import requests
import os
from datetime import datetime,timedelta



KIWI_ENDPOINT = "https://api.tequila.kiwi.com"

class FlightSearch:
    """
    This class is responsible for interacting with the Flight Search API to find flight details.

    Attributes:
        key (str): API key for Flight Search API.
        endpoint (str): Endpoint URL for the API.
        fly_from (str): IATA code of the departure city.
        fly_to (str): IATA code of the destination city.
        date_from (str): Start date for the flight search.
        date_to (str): End date for the flight search.
        curr (str): Currency in which prices should be displayed.
        flight_details (dict): Details of the found flights.

    Methods:
        get_flights: Performs a flight search and returns the results.
    """
    
    def __init__(self, destination:str) -> None:
        self.key = os.environ.get('KIWI_KEY')
        self.endpoint = KIWI_ENDPOINT
        self.fly_from = 'AMS'
        self.fly_to = destination.upper()
        self.date_from = (datetime.now() + timedelta(1)).strftime("%d/%m/%Y") # Search from tomorrow
        self.date_to = (datetime.now() + timedelta(180)).strftime("%d/%m/%Y") # Up to 6 months from now

        self.curr = "EUR" # Currency
        self.flight_details = self.get_flights()
            
    def get_flights(self):
        search_url = f"{self.endpoint}/v2/search"
        headers = {'apikey': self.key}
        parameters ={
            'fly_from': 'AMS',
            'fly_to': self.fly_to,
            'date_from': self.date_from,
            'date_to': self.date_to,
            'nights_in_dst_from': 7,
            'nights_in_dst_to': 28,
            'flight_type': "round",
            'curr': self.curr,
            'one_for_city': 1,
            'max_stopovers': 2, # You can change it to 0 if you want direct flights!
            'limit': 1, # Returns only the cheapest option
        }
        response = requests.get(url=search_url, headers=headers, params=parameters)
        response.raise_for_status()
        data = response.json()
        return data



