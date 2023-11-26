# Movie Titles Scraper
## Description

This Python script is a simple web scraping application designed to extract a list of movie titles from a specific URL (an archived Empire Online article) and save these titles  a text file. It uses the requests library to fetch the webpage and BeautifulSoup from bs4 for parsing HTML content.

## Requirements
- Python 3.x
- requests library
- beautifulsoup4 library

## Installation

Before running the script, ensure you have Python installed on your system. Then, install the required libraries using pip:


`pip install requests beautifulsoup4`

## Usage
To run the script, simply execute it with Python:

`python movie_titles_scraper.py`

The script will create a file movies.txt in the movies_scrapper directory, containing the list of movie titles in reverse order.

## Disclaimer

This script is for educational purposes only. Ensure you have permission to scrape any website and that your actions comply with the website's terms of service or usage policies.

