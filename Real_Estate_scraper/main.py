import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, StaleElementReferenceException
from fake_useragent import UserAgent
import time
from bs4 import BeautifulSoup
from pprint import pprint
import pandas as pd


FUNDA_URL ='https://www.funda.nl/'
BUY_OR_RENT = "/huur"
AREA = "Leiden"
# Before entering your preferences check available options on the website
SEARCH_RANGE = "10" # In KM 
MAX_PRICE = "1500" # In Euro


GOOGLE_FORM_LINK = '' # YOU SHOULD UPDATE WITH THE LINK OF THE GOOGLE FORM YOU HAVE CREATED!
EXCEL_FILE = 'search_results.xlsx'

# Set Brave's path for macOS
brave_path = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"
ua = UserAgent(os='macos')
user_agent = ua.random

# Keep chrome window open
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = brave_path
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument(f"--user-agent={user_agent}")

class WebsiteInteractionManager:
    """
    Manages interactions with a real estate website using Selenium.

    This class automates the process of setting up a browser session,
    navigating through the website, filling out search parameters,
    and handling page navigation.

    Attributes:
        driver (webdriver): A Selenium WebDriver to automate browser actions.
    """

    # You need to be fast with the Catcha...
    def __init__(self) -> None:
        self.driver =webdriver.Chrome(options=chrome_options)
        self.driver.get(FUNDA_URL)
        time.sleep(30)
    
    def fill_search_parameters(self):
        """
        Fills out the search parameters on the website.

        This method automates the process of selecting search options like
        house type, area, search range, and maximum price, and then submits the search.
        """
        try:
            # Chose rent or buy. Netherlands for the test
            house_type = self.driver.find_element(By.XPATH, value='/html/body/main/div[1]/div[3]/form/nav/ul/li[2]/a')
            house_type.click()
            time.sleep(5)
            # Search Area
            area_box = self.driver.find_element(By.XPATH, value='/html/body/main/div[1]/div[3]/form/div/div[1]/fieldset[1]/div[1]/input[3]')
            area_box.send_keys(AREA)
            time.sleep(5)
            
            # Search area range
            search_range_dropdown = Select(self.driver.find_element(By.ID, value='Straal'))
            search_range_dropdown.select_by_value(SEARCH_RANGE)
            time.sleep(5)
            
            # Maximum price
            max_price_dropdown = Select(self.driver.find_element(By.ID, value='range-filter-selector-select-filter_huurprijstot'))
            max_price_dropdown.select_by_value(MAX_PRICE)
            time.sleep(5)
            
            # submit search parameters
            submit_search = self.driver.find_element(By.XPATH, value='/html/body/main/div[1]/div[3]/form/div/div[1]/div/button')
            submit_search.click()
            
            print("The search is done!")
            time.sleep(10)
        except Exception as e:
            print(f"Error while filling search parameters: {e}")
            self.quit()
    
    def next_page(self):
        """
        Navigates to the next page of search results if available.
        This is happening by checking the last clickable item of the list (-> called: Volgende) 
        then will checks if the value is 0(Active) or -1(Disabled) and will click it 
        Returns:
            bool: True if the next page is available and clicked, False otherwise.
        """

        try:
            next_page = self.driver.find_elements(By.CSS_SELECTOR, value='.pagination li a')
                
            if next_page[-1].get_attribute('tabindex') == '0':
                next_page[-1].click()
                return True
            else:
                print('No more pages!')
                return False
        except Exception as e:
            print(f"Error while navigating to the next page: {e}")
            return False


    def quit(self):
        self.driver.quit()
        
    def page_source(self):
        # We return the page source to be used in Beautiful soup!
        return self.driver.page_source
    
class RealEstateWebsiteScraper:
    """
    Scrapes real estate listing data from a webpage.

    Parses the HTML content of a real estate listings page using BeautifulSoup
    to extract relevant data like property address, price, and links.

    Attributes:
        soup (BeautifulSoup): A BeautifulSoup object to parse HTML.
        elements (list): A list of tuples containing scraped data.
    """
    def __init__(self, page) -> None:
        self.soup = BeautifulSoup(page, 'lxml')
        self.elements = self.create_elements_list()
    
    def find_href_elements(self) -> list:
        try:
            href_elements = self.soup.find_all('a',attrs={"data-test-id":"object-image-link"}) # The picture link and the name link are the same...for now
            href_list = [link.get('href') for link in href_elements]
            return href_list
        except Exception as e:
            print(f"Error in find_href_elements: {e}")
            return []
        
        
    def find_text_elements(self, search_attributes:dict) -> list:
        try:
            text_elements = self.soup.find_all(attrs=search_attributes)
            elements_list = [street.get_text() for street in text_elements]
            cleaned_list = self.remove_garbage_chars(elements_list) # Removes the extra characters and the white space
            return  cleaned_list
        except Exception as e:
            print(f"Error in find_text_elements: {e}")
            return []

    def create_elements_list(self) -> list:
        # Get href elements
        href = self.find_href_elements()
        # Get the street address
        streets = self.find_text_elements(search_attributes={"data-test-id": "street-name-house-number"})
    
        # Get the postal Code
        postal_codes = self.find_text_elements(search_attributes={"data-test-id": "postal-code-city"})
        
        # Get prices
        prices = self.find_text_elements(search_attributes={"data-test-id": "price-rent"})
        prices_cleaned = self.numbers_only(list=prices) # In order to keep only the numerical value
        
        # Combine all the lists in one list
        elements_list = list(zip(streets, postal_codes, prices_cleaned, href))
        
        return elements_list
    
    def remove_garbage_chars(self, list:list) -> list:
        cleaned_list = [item.strip() for item in list]
        cleaned_list = [re.sub(r'[^\w\s]', '', item) for item in cleaned_list]
        return cleaned_list
    
    def numbers_only(self, list:list) -> list:
        cleaned_list = [re.sub(r'\D', '', item) for item in list]
        return cleaned_list
        
    def get_offers_list(self) -> list:
        return self.elements


class DataManipulation:
    """
    Handles data manipulation for the scraped real estate data.

    This class provides functionality to store the scraped data in a structured format,
    and to output the data to an Excel file.

    Attributes:
        scraped_data (dict): A dictionary to store the scraped data.
    """
    def __init__(self) -> None:
        self.scraped_data = {"Address": [],
                     "Price": [],
                     "Link": [],
                     }
        
    def add_data_in_dictionary(self, elements_list:list) -> dict:
        # We append all the data we collected from each page in a dictionary and then return it back .replace('(', '').replace(')', '').replace('"', '')
        for entry in elements_list:
            self.scraped_data["Address"].append(f"{entry[0]}, {entry[1]}")
            self.scraped_data["Price"].append(f"{entry[2]}")
            self.scraped_data["Link"].append(f"{entry[3]}")
   
    def to_excel_file(self):
        df = pd.DataFrame(self.scraped_data)
        df.to_excel(EXCEL_FILE, index=False)
        

class GoogleFormFiller:
    """
    Automates data entry into a Google Form.

    Uses Selenium to automate the process of entering scraped data into a specified
    Google Form.

    Attributes:
        driver (webdriver): A Selenium WebDriver to automate browser actions.
    """
    def __init__(self) -> None:
        self.driver =webdriver.Chrome(options=chrome_options)
        self.driver.get(GOOGLE_FORM_LINK)
        
    def submit_listing_to_form(self, address:str, price:str, link:str):
        try:
            time.sleep(2)
            address_element = self.driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            price_element = self.driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            link_element = self.driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
            submit_element = self.driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
            
            address_element.send_keys(address)
            time.sleep(0.3)
            price_element.send_keys(price)
            time.sleep(0.3)
            link_element.send_keys(link)
            time.sleep(0.3)
            submit_element.click()
            time.sleep(2)
            self.driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a').click() # Move to next input
            
        except Exception as e:
            print(f"There was an issue {str(e)}")
    
    def quit(self):
        self.driver.quit()
            
    
def main():

    new_search = WebsiteInteractionManager()
    new_search.fill_search_parameters()
    time.sleep(5)
    
    
    search_results = DataManipulation()
    go_on = True

    while go_on:
        
        soup = RealEstateWebsiteScraper(new_search.page_source())
        # Create a combined list to upload in google sheets
        search_results.add_data_in_dictionary(elements_list=soup.elements)
        time.sleep(10)
        go_on = new_search.next_page()
    
    search_results.to_excel_file()
    results = search_results.scraped_data
    google_form_entry = GoogleFormFiller()
    time.sleep(10)
    
    # Need to check if the form is working while doing inputs.
    for listing in range(len(results["Address"])):
        address = results["Address"][listing]
    
        price = results["Price"][listing]
        link = results["Link"][listing]
        google_form_entry.submit_listing_to_form(address=address, price=price, link=link)
        time.sleep(5)
    
   
    print("Scraping the pages is done\n You can now find all the data in the form or excel file. Terminating program in 10 secs!")
    
    time.sleep(10)
    new_search.quit()
    google_form_entry.quit()


if __name__ == "__main__":
    main()