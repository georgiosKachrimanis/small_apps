import requests
import os
from bs4 import BeautifulSoup
import smtplib


# I use the Dutch store as I am located here, you can adjust accordingly
AMAZON_BASE_URL = "https://www.amazon.nl/" 

# Email credentials and SMTP server configuration.
MY_MAIN_EMAIL = os.environ.get('MY_MAIN_EMAIL')
MY_SECONDARY_EMAIL = os.environ.get('MY_SECOND_EMAIL')
MY_PASSWORD = os.environ.get("MY_SECOND_EMAIL_KEY")  # The smtp service providers can create an one time password to use to lod in the email API. You can find more information with some google search!
MY_SMTP_SERVER = os.environ.get("MY_SMTP_SERVER") # Depending on the email service you are using you must change this!
SUBJECT = "Subject:Low Price Alert for one of your products!\n\n" # Email subject line for the birthday message.

# You should check your headers and webbrowser to change them accordingly.
headers = {"Accept-Language": "en-GB,en;q=0.8",
           "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8", 
           "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"   
}


def amazon_search(item_url:str):
    """
    Fetches the content from Amazon page for the given item URL.

    Args:
    item_url (str): Specific part of the URL corresponding to the product.

    Returns:
    BeautifulSoup object: Parsed HTML content of the product page.
    """
    
    response = requests.get(url=AMAZON_BASE_URL+item_url, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")
    return soup

def price_check(soup:BaseExceptionGroup, alert_price:float):
    """
    Checks the price of a product and sends an email notification if the price is below the alert price.

    Args:
    soup (BeautifulSoup): Parsed HTML content of the product page.
    alert_price (float): The threshold price to trigger the alert.

    Returns:
    None
    """
    
    # Get the price, then the text and remove the euro sign, replace the coma with point and finally make it into a float
    product_title = soup.find(id='productTitle').getText()
    price = float(soup.find(id='price').getText().split("€")[1].replace(",", "."))
    if price < alert_price:
        send_notifications(f"{product_title} today is at : {price} euro in Amazon.")


def send_notifications(email_text:str):
    """
    Sends an email notification with the specified text.

    Args:
    email_text (str): The content of the email to be sent.

    Returns:
    None
    """
    with smtplib.SMTP(MY_SMTP_SERVER, port=587) as connection:
        connection.starttls()  # Secure the connection with TLS
        connection.login(user=MY_SECONDARY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_SECONDARY_EMAIL,to_addrs=MY_MAIN_EMAIL,msg=f"{SUBJECT}{email_text}")


def main():
    
    # Change the url of the product you want to check
    product_url = "Clean-Coder-Conduct-Professional-Programmers/dp/0137081073/ref=sr_1_4?keywords=Robert+martin&qid=1701242006&sr=8-4"
    search_results = amazon_search(product_url)
    # Change the maximum price for the product you are looking for
    maximum_price = 25.00
    price_check(soup=search_results, alert_price=maximum_price)
    
    
if __name__=="__main__":
    main()