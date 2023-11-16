from flight_search import FlightSearch

#This class is responsible for structuring the flight data.
class FlightData:
    """
    This class is responsible for structuring the flight data obtained from the Flight Search API.

    Attributes:
        price (int): Price of the flight.
        fly_from (str): IATA code of the departure city.
        city_name_from (str): Name of the departure city.
        fly_to (str): IATA code of the destination city.
        city_name_to (str): Name of the destination city.
        outbound_date (str): Departure date.
        inbound_date (str): Return date.

    Methods:
        flight_details: Returns a string with detailed information about the flight deal.
    """
    def __init__(self, result:FlightSearch) -> None:
        self.price = int(result.flight_details['data'][0]['price'])
        self.fly_from = result.flight_details['data'][0]['flyFrom']
        self.city_name_from = result.flight_details['data'][0]['cityFrom']
        self.fly_to = result.flight_details['data'][0]['flyTo']
        self.city_name_to = result.flight_details['data'][0]['cityTo']
        self.outbound_date = result.flight_details['data'][0]['local_departure'].split("T")[0] # Need to change to European :p
        self.inbound_date = result.flight_details['data'][0]['route'][-1]['local_arrival'].split("T")[0] # Need to change to European :p
    
    def flight_details(self):
        return f"Low price alert! Only {self.price} euro to fly from {self.city_name_from}-{self.fly_from} to {self.city_name_to}-{self.fly_to}, from {self.outbound_date} until {self.inbound_date}."


