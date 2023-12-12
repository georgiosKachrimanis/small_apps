from selenium import webdriver
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
import time

# Set Brave's path for macOS. If you are using a different browser, please check the documentation.
brave_path = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"
ua = UserAgent(os="macos")
user_agent = ua.random

# Keep Chrome/Brave window open with custom options.
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = brave_path
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument(f"--user-agent={user_agent}")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")


# List of store items by their HTML ID.
STORE_ITEMS = [
    "buyCursor",
    "buyGrandma",
    "buyFactory",
    "buyMine",
    "buyAlchemy lab",
    "buyShipment",
    "buyTime machine",
    "buyElder pledge",
]


def get_store_prices():
    """
    Retrieves the prices of items available in the store.

    :return: A list of integers representing the prices of each store item.
    """
    store_elements = driver.find_elements(By.CSS_SELECTOR, value="#store b")
    prices = []

    for item in store_elements:
        if item.text:
            prices.append(int(item.text.split()[-1].replace(",", "")))

    return prices


def buy_store_upgrade(current_cookies: int, current_store_prices: list):
    """
    Buys the best store upgrade based on the current number of cookies and store prices.
    Chooses the most expensive item that can be afforded, but does not perform an action if no item is affordable.

    :param current_cookies: The current number of cookies available.
    :param current_store_prices: A list of prices for each store upgrade.
    """
    best_option = None
    max_price = 0

    # Iterate through store prices to find the best upgrade option
    for index, price in enumerate(current_store_prices):
        if price <= current_cookies and price > max_price:
            best_option = index
            max_price = price

    # Click on the best upgrade option if it exists and is affordable
    if best_option is not None:
        store_upgrade = driver.find_element(By.ID, value=STORE_ITEMS[best_option])
        store_upgrade.click()


def get_cookie_count():
    """
    Retrieves the current count of cookies.

    :return: The number of cookies available as a string.
    """
    available_cookies = driver.find_element(By.ID, value="money")
    return available_cookies.text.replace(",", "")


# Main cookie clicker interaction element.
cookie_clicker = driver.find_element(By.ID, value="cookie")

# Timers for periodic checks and end of the game.
five_seconds_check = time.time() + 5
end_of_game_timer = time.time() + 300

while True:
    # Click the cookie.
    cookie_clicker.click()

    # Every five seconds, check for available upgrades and buy the best one.
    if time.time() > five_seconds_check:
        store_prices = get_store_prices()
        available_cookies = int(get_cookie_count())
        buy_store_upgrade(
            current_cookies=available_cookies, current_store_prices=store_prices
        )
        five_seconds_check = time.time() + 5

    # End the game after a specified duration and print cookies per second.
    if time.time() >= end_of_game_timer:
        cookies_per_second = driver.find_element(By.ID, value="cps")
        print(f"Cookies per second: {cookies_per_second.text}")
        break

# Close the browser session.
driver.quit()
