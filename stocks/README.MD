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
git clone https://github.com//stock-news-alert.git
cd stock-news-alert