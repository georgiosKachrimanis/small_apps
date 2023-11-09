# RainApp

RainApp is a simple Python application that checks the weather forecast and sends an SMS alert if rain is expected within the next 12 hours.

## Features

- Uses OpenWeatherMap API to fetch the latest weather forecast.
- Sends an alert via SMS using Twilio's messaging API if rain is predicted.

## Requirements

- Python 3
- `requests` library
- A Twilio account with an active phone number
- An OpenWeatherMap API key

## Environment Setup

Set the following environment variables:

- `TWILIO_ACCOUNT_SID`: Your Twilio Account SID
- `TWILIO_AUTH_TOKEN`: Your Twilio Auth Token
- `TWILIO_NUMBER`: Your Twilio phone number
- `MY_NUMBER`: The phone number where you wish to send the alert
- `OWM_API_KEY`: Your OpenWeatherMap API key
- `LAN and LON`: Depending on the city/area you want to get alerts.

## Usage

1. Install the required Python libraries.
2. Clone the repository and navigate to the app directory.
3. Of course you must have created accounts both in OpenWeatherMap and Twilio
3. Run the script.


If rain is forecasted within the next 12 hours, you will receive an SMS alert.

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

- Georgios Kachrimanis 
- Project Link: [https://github.com/georgiosKachrimanis/rainapp](https://github.com/georgiosKachrimanis/rainapp)

