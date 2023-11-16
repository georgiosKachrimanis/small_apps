import requests
import os

#This class is responsible for talking to the Google Sheet.
class DataManager:
    """
    This class is responsible for communicating with the Google Sheet containing flight deal information.
    It fetches and stores the current destinations and their associated details.

    Attributes:
        password (str): Password for Sheety API access.
        user (str): User name for Sheety API access.
        endpoint (str): Endpoint URL for the Google Sheet.
        current_destinations (list): List of current destinations with their IATA codes and target prices.

    Methods:
        get_destinations: Fetches the current destinations from the Google Sheet and returns them as a list.
    """
    def __init__(self) -> None:
        self.password = os.environ.get('SHEETY_PASS')
        self.user = os.environ.get('SHEETY_USER')
        self.endpoint = "https://api.sheety.co/2b8b564dbc8b5e35348b478b9f9509ff/flightDeals/prices"
        self.current_destinations = self.get_destinations()
         
    def get_destinations(self):
        response = requests.get(self.endpoint, auth=(self.user, self.password))
        response.raise_for_status()
        data = response.json()
        data = data['prices']
        data_list = [{'iataCode': destination['iataCode'], 'price': destination['price']} for destination in data]
        return data_list
        