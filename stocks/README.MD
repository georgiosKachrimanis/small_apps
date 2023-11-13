# Stock News Alert Application

This repository contains a Python application designed to monitor stock price changes and send SMS alerts with relevant news articles when significant changes are detected. The application focuses on Tesla Inc (TSLA) but can be modified for other stocks.

## Features

- Tracks daily stock prices using the Alpha Vantage API.
- Fetches recent news articles related to Tesla Inc from the News API.
- Sends SMS alerts for significant stock price changes with relevant news headlines and descriptions.
- Utilizes Twilio's API for sending SMS alerts.

## Requirements

- Python 3
- Requests library
- Twilio Python library
- An Alpha Vantage API key
- A News API key
- A Twilio account with an authenticated phone number

## Setup

1. **Clone the repository:**
`git clone https://github.com/georgiosKachrimanis/small_apps.git`
`cd stocks`

2. **Install dependencies:**
`pip install requests twillio`


3. **Set Environment Variables:**
- Set the following environment variables with the respective API keys and Twilio account details:
  - `ALPHA_VANTAGE_API`: Your Alpha Vantage API key.
  - `NEWS_API_KEY`: Your News API key.
  - `TWILIO_ACCOUNT_SID`: Your Twilio Account SID.
  - `TWILIO_AUTH_TOKEN`: Your Twilio Auth Token.
  - `TWILIO_NUMBER`: Your Twilio phone number.
  - `MY_NUMBER`: The phone number to receive the alerts.

4. **Run the application:**

`python3 stocks.py`


## Usage

The application checks the latest stock price of Tesla Inc and compares it with the previous day's price. If the change is significant (more than 5% by default), it fetches the latest news articles related to Tesla Inc and sends an SMS alert with the news information.

If you want to check another stock, ou can just change the name of the company and stock!

## Contributing

Contributions are welcome! Please feel free to submit pull requests, create issues, or provide feedback.


## Contact

- Try to find me in LinkedIn if you want to contact me!
- Project Link: [https://github.com/georgiosKachrimanis/small_apps](https://github.com/georgiosKachrimanis/small_apps)

---

> Note: This application is for educational purposes only. Always ensure compliance with the APIs' terms of use and avoid sharing sensitive personal information.
