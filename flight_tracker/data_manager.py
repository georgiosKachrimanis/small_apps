import requests
import os
from flight_search import FlightSearch
import re

#This class is responsible for talking to the Google Sheet.
class DataManager:
    """
    Handles data retrieval and updates with a Google Sheet (or similar) for flight deals.

    Attributes:
        flight_search (FlightSearch): An instance of FlightSearch for IATA code lookup.
        password (str): Authentication password for accessing the data sheet.
        user (str): Username for accessing the data sheet.
        endpoint (str): API endpoint for the data sheet.

    Methods:
        get_destinations(): Retrieves current destination data from the data sheet.
        add_destination(city_name, price): Adds a new destination to the data sheet.
        collect_user_data(): Collects user data interactively and stores it.
        user_email_check(): Validates user email through interactive input.
        is_email_valid(email): Checks if the provided email is valid.
        add_user(first_name, last_name, email, origin): Adds a new user to the data sheet.
        get_email_list(): Retrieves a list of emails for notification.
    """
    def __init__(self, flight_search:FlightSearch) -> None:
        self.flight_search = flight_search
        self.password = os.environ.get('SHEETY_PASS')
        self.user = os.environ.get('SHEETY_USER')
        self.endpoint = "https://api.sheety.co/2b8b564dbc8b5e35348b478b9f9509ff/flightDeals"
        # self.current_destinations = self.get_destinations()
         
    def get_destinations(self):
        prices_endpoint = f"{self.endpoint}/prices"
        response = requests.get(prices_endpoint, auth=(self.user, self.password))
        response.raise_for_status()
        data = response.json()
        data = data['prices']
        data_list = [{'iataCode': destination['iataCode'], 'price': destination['price']} for destination in data]
        return data_list
    
    def add_destination(self, city_name:str, price:int):
        prices_endpoint = f"{self.endpoint}/prices"
        iata_code = self.flight_search.get_destination_IATA_code(city_name=city_name)
        query = {
            'price':
                {'city': city_name, 
                 'iataCode': iata_code, 
                 'price': price}
            }
        
        response = requests.post(prices_endpoint, auth=(self.user, self.password), json=query)
        response.raise_for_status()
        print(response.status_code)
                      

    def collect_user_data(self):      
            first_name = input("What is your first name?\n").title()
            last_name = input("What is your last name?\n").title()
            origin = input("Where do you usually travel from?\n").title()
            
            email = self.user_email_check()
            if email:
                self.add_user(first_name=first_name, last_name=last_name, email=email, origin=origin)
            
    def user_email_check(self):
        
        while True:
            email1 = input("What is your email?\n").strip()
            if email1.lower() in ('quit','exit'):
                exit()
                
            email2 = input("Type your email again?\n").strip()
            if email2.lower() in ('quit','exit'):
                exit()
                
            if email1 == email2:
                if self.is_email_valid(email=email1):
                    return email1
                else:
                    print("The email is not valid, please try again!")
            else:
                print("The emails are different try again please!")
                        
    
    def is_email_valid(self, email):
        pattern = pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return re.match(pattern, email) is not None
    
    
    def add_user(self, first_name:str, last_name:str, email:str, origin:str):
        users_endpoint = f"{self.endpoint}/users"
        query = {
            'user':{
            'firstName': first_name,
            'lastName': last_name,
            'email': email,
            'origin': origin
            }
        }
        
        response = requests.post(users_endpoint, auth=(self.user, self.password), json=query)
        response.raise_for_status()
        
        if 200 <= response.status_code <300:
            print(f"{first_name} {last_name} have been added successfully in the mailing list.")
       
       
    def get_email_list(self):
        users_endpoint = f"{self.endpoint}/users"
        response = requests.get(users_endpoint, auth=(self.user, self.password))
        response.raise_for_status()
        data = response.json()
        data = data['users']
        data_list = [{'First Name': user['firstName'], 'Last Name': user['lastName'], 'Email': user['email'], 'Origin': user['origin']} for user in data]
        return data_list
        







