import datetime
import requests
import os
from twilio.rest import Client

STOCK_NAME = "TSLA" # Change the stock name here!
COMPANY_NAME = "Tesla Inc" # Change the company name here!

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

alpha_vantage_api_key = os.environ.get("ALPHA_VANTAGE_API")
news_api_key = os.environ.get("NEWS_API_KEY")

is_up = False # If the stock was up or down the last 2 days!

account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
twilio_number = os.environ.get("TWILIO_NUMBER")
my_number = os.environ.get("MY_NUMBER")

def day_check(input_date: datetime.date) -> datetime.date:
    """
    Adjust the input date to the last weekday if it falls on a weekend.

    Args:
        input_date (datetime.date): The date to be checked.

    Returns:
        datetime.date: The adjusted date.
    """
    if input_date.weekday() > 4:  # Saturday=5, Sunday=6
        return input_date - datetime.timedelta(days=input_date.weekday() - 4)
    return input_date


def calculate_percentage(yesterday: float, day_before_yesterday: float) -> float:
    """
    Calculate the percentage change between two values.

    Args:
        yesterday (float): The recent value.
        day_before_yesterday (float): The earlier value.

    Returns:
        float: The percentage change.
    """
    global is_up
    if yesterday >= day_before_yesterday:
        is_up = True
        return abs(day_before_yesterday / yesterday - 1)
    else:
        is_up = False
        return abs(yesterday / day_before_yesterday - 1)
    

def create_requests(endpoint_url: str, parameters: dict) -> dict:
    """
    Make a GET request to a specified endpoint with given parameters.

    Args:
        endpoint_url (str): The API endpoint URL.
        parameters (dict): The parameters for the API request.

    Returns:
        dict: The JSON response data.
    """
    response = requests.get(endpoint_url, params=parameters)
    response.raise_for_status()
    return response.json()


def stock_information() -> dict:
    """
    Fetches the stock information for a specified stock symbol.

    Returns:
        dict: The stock information data.
    """
    stocks_parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK_NAME,
        "apikey": alpha_vantage_api_key,
    }

    stocks_data = create_requests(endpoint_url=STOCK_ENDPOINT, parameters=stocks_parameters)
    data = stocks_data['Time Series (Daily)']
    return data


def get_news_articles() -> list:
    """
    Fetches news articles related to the company.

    Returns:
        list: A list of news articles.
    """
    news_parameters = {
        "q": COMPANY_NAME,
        "apikey": news_api_key,
    }

    news_data = create_requests(endpoint_url=NEWS_ENDPOINT, parameters=news_parameters)
    return [news_data['articles'][i] for i in range(3)]


def send_sms(sms_body: str):
    """
    Sends an SMS with the given message body.

    Args:
        sms_body (str): The body of the SMS message.
    """
    client = Client(account_sid, auth_token)
    message = client.messages.create(
                        body=sms_body,
                        from_=twilio_number,
                        to=my_number
                    )
    print(message.status)

stock_info = stock_information()

yesterday = day_check(datetime.date.today() - datetime.timedelta(days=1)) # We need to check if yesterday or the day before are during weekends
day_before_yesterday = day_check(yesterday - datetime.timedelta(days=1))
closing_price_minus_one = float(stock_info[str(yesterday)]['4. close'])
closing_price_minus_two = float(stock_info[str(day_before_yesterday)]['4. close'])

# Also you can make your life easier and instead of checking the dates, just take the last two values of the dictionaries
# stock_prices_list = [value for (key, value) in stock_info.items()]
# data_yesterday = stock_prices_list[0]
# yesterday_closing = data_yesterday["4. close"]
# data_day_before_yesterday = stock_prices_list[1]
# day_before_yesterday_closing = data_day_before_yesterday["4. close"]
# print(yesterday_closing, day_before_yesterday_closing)

percent_change = calculate_percentage(yesterday=closing_price_minus_one, day_before_yesterday=closing_price_minus_two)

# You can find the percentage value by doing the following! divide the difference of the 2 prices and the closing price from yesterday
day_difference = abs(closing_price_minus_one - closing_price_minus_two)
diff_percent = day_difference /closing_price_minus_one * 100


if percent_change <= 0.05: # For testing reasons
    news = get_news_articles()        
    news_list = [[article['title'], article['description']] for article in news]
    
    if is_up:
        stock_marking = '🔺'
    else:
        stock_marking = '🔻'
    
    for article in news_list:
        sms_txt = f"{STOCK_NAME}: {stock_marking}{percent_change*100:.2f}%\nHeadline: {article[0]}\nBrief: {article[1]}\n"
        send_sms(sms_txt)
    
    

