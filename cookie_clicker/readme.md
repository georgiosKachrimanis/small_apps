# Cookie Clicker Bot

## Overview
This Cookie Clicker Bot is a simple automation script developed in Python, utilizing Selenium WebDriver. It's designed for educational purposes to demonstrate web automation and interaction with web elements. The bot plays the Cookie Clicker game (https://orteil.dashnet.org/experiments/cookie/) by automatically clicking on the cookie and purchasing store upgrades.

## Prerequisites
To run this bot, you'll need:

Python 3.x
Selenium WebDriver
ChromeDriver (or BraveDriver if using Brave)
Fake UserAgent
Setup

## Install Python Packages:

`pip install selenium fake_useragent`

Download ChromeDriver:

Download the appropriate version of ChromeDriver from ChromeDriver - WebDriver for Chrome. 

If you're using Brave browser, the ChromeDriver should be compatible. Ensure it's in your PATH or specify its location in the script.

Set Browser Path:
Update the brave_path in the script to match the location of Brave on your system. For Chrome, adjust the setup accordingly.

## Usage
Run the script with Python:


`python main.py`

The bot will start the Cookie Clicker game in a browser window and begin clicking on the cookie. It will periodically check for and purchase the best available store upgrade based on the current number of cookies.

## How it Works

The bot clicks on the cookie at the center of the game.
Every 5 seconds, it checks the number of cookies and compares it with the store items' prices.
It purchases the most expensive affordable upgrade to maximize cookie production.
After a set duration (default 300 seconds), the bot will print the cookies per second rate and end the game.

# Note
This bot is created for educational purposes and serves as a basic example of using Selenium for web automation. Please refer to the Selenium with Python documentation for more detailed information on Selenium WebDriver.

# License
This project is open-sourced under the MIT license.