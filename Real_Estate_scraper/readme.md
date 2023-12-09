# Real Estate Web Scraper

This project is a Python-based web scraping tool that automates the process of collecting real estate listings from a website. It uses Selenium for browser automation and BeautifulSoup for parsing HTML content. The scraped data is structured and saved into an Excel file and also entered into a Google Form.

**Important Notice: You will have to manage the cookies and captcha your self. (30 seconds timer)**

## Features

- Automated navigation of real estate listing website.
- Customizable search parameters for property listings.
- Scraping of important details like address, price, and links.
- Data export to an Excel file.
- Automated data entry into a Google Form.

## Prerequisites

Before running this application, ensure you have the following installed:
- Python 3.x
- Selenium
- BeautifulSoup
- pandas
- Other dependencies listed in `requirements.txt`.

## Installation

1. Clone the repository:

   `git clone [repository-url]`
2. Navigate to the cloned directory and install the required Python packages:

    `pip install -r requirements.txt`

## Usage

1. Configure the search parameters in the script according to your requirements.
2. Run the script:

    `python main.py`
3. The script will start the web scraping process, and the results will be saved in an Excel file and entered into the specified Google Form.

## Configuration

You can modify the following variables in the script to customize the search:

- FUNDA_URL: URL of the real estate website.
- BUY_OR_RENT: Specify whether to search for properties to buy or rent.
- AREA: Area of interest for property listings.
- SEARCH_RANGE: Radius in kilometers for the search.
- MAX_PRICE: Maximum price of properties.
- GOOGLE_FORM_LINK: URL of the Google Form for data entry.
- EXCEL_FILE: Name of the Excel file for saving the data.

## Google Forms Setup:

1. Open Google Forms:

- Go to Google Forms.
- If you're not already signed in, sign in with your Google account.

2. Start a New Form:

- Click on the + button to create a new form.
- You can also choose a template if you prefer, but for this purpose, a blank form should suffice.

3. Set Up the Form:

- Give your form a title, like "Real Estate Listings."
- Optionally, add a description to provide context about the form.

4. Add Questions:

- Click on the + button on the right sidebar to add a new question.
- You'll need to add at least three questions for Address, Price, and Link.

5. Configure Question for Address:

- Set the question title to "Address".
- Change the question type to "Short answer" (as addresses can be lengthy).
- You can make this a required question by toggling the "Required" button.

6. Configure Question for Price:

- Set the question title to "Price".
- Change the question type to "Short answer" as well.
- Ensure it's marked as "Required" if necessary.

7. Configure Question for Link:

- Set the question title to "Listing Link".
- Set the question type to "Short answer" to paste the URL.
- This can also be a required question.

8. Saving and Sharing the Form:

- Google Forms auto-saves your form.
- Click on the "Send" button to share your form. You can send it via email, share a link, or even embed it on a website.

9. Retrieving Responses:

- Responses to your form will be collected in the "Responses" tab.
- You can also link these responses to a Google Sheets spreadsheet for easier analysis and manipulation.

10. You can also create a google sheet and save the responses there every time you run the app:
- At the Form page, click on the Responses.
- You will see Link to Sheets
- Create new spreadsheet and name it what ever you like.
- Enjoy!

## Important Notes
- This tool is intended for educational purposes and should be used responsibly.
- Make sure to comply with the website’s terms of service when scraping.

## License

This project is licensed under the MIT License.

## Acknowledgements

- This project was created for educational purposes and is not endorsed by any real estate websites.