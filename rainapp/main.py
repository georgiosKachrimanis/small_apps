import requests
from twilio.rest import Client
import os

def send_rain_alert():
    """
    Checks weather forecast for rain and sends an SMS alert if rain is expected.

    This script uses OpenWeatherMap's API to fetch the weather forecast for a specific
    location and checks the next 12 hours for any weather conditions with IDs less than 700,
    which generally indicate precipitation. If rain is expected, it sends an SMS alert
    using Twilio's messaging service.

    Environment Variables:
        - TWILIO_ACCOUNT_SID: Your Twilio Account SID
        - TWILIO_AUTH_TOKEN: Your Twilio Auth Token
        - TWILIO_NUMBER: Your Twilio phone number
        - MY_NUMBER: The phone number where you wish to send the alert
        - OWM_API_KEY: Your OpenWeatherMap API key

    Returns:
        None
    """

    # Find your Account SID and Auth Token at twilio.com/console
    # and set the environment variables. See http://twil.io/secure
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    twilio_number = os.environ['TWILIO_NUMBER']
    my_number = os.environ['MY_NUMBER']

    owm_key = os.environ['OWM_API_KEY']  # API key for OpenWeatherMap.org.
    owm_endpoint = "https://api.openweathermap.org/data/3.0/onecall"

    # Coordinates for the city place you want to check.
    LAT = ""
    LON = ""

    parameters = {
        "lat": LAT,
        "lon": LON,
        "exclude": ["current,minutely,daily"],
        "appid": owm_key,
    }

    response = requests.get(owm_endpoint, params=parameters)
    response.raise_for_status()

    weather_data = response.json()
    slice_12_hours = weather_data['hourly'][:12]

    will_rain = any(int(hour_data['weather'][0]['id']) < 700 for hour_data in slice_12_hours)

    if will_rain:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body="It is going to rain later today, so bring your ☔️",
            from_=twilio_number,
            to=my_number
        )
        print(message.status)

# Main execution
if __name__ == "__main__":
    send_rain_alert()
