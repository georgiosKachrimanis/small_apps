import requests
import os
from datetime import datetime, timedelta
from requests.exceptions import HTTPError, RequestException
import json
import pprint
from flight_data import FlightData


KIWI_ENDPOINT = "https://api.tequila.kiwi.com"


class FlightSearch:
    """
    Searches for available flights using the Kiwi API.

    Attributes:
        headers (dict): Headers for the API requests, including the API key.
        endpoint (str): Base endpoint URL for the Kiwi API.
        curr (str): Currency to be used in flight searches.

    Methods:
        get_destination_IATA_code(city_name): Returns the IATA code for a given city name.
        check_available_flights(origin_city_code, destination_city_code, date_from, date_to):
            Checks for available flights between two cities within given dates.
    """

    def __init__(self) -> None:
        self.headers = {"apikey": os.environ.get("KIWI_KEY")}
        self.endpoint = KIWI_ENDPOINT
        self.curr = "EUR"  # Currency

    def get_destination_IATA_code(self, city_name):
        location_endpoint = f"{self.endpoint}/locations/query"
        query = {"term": city_name, "location_types": "city"}
        response = requests.get(
            url=location_endpoint, headers=self.headers, params=query
        )
        results = response.json()["locations"]
        iata_code = results[0]["code"]
        return iata_code

    def check_available_flights(
        self,
        origin_city_code: str,
        destination_city_code: str,
        date_from: datetime,
        date_to: datetime,
    ):
        search_url = f"{self.endpoint}/v2/search"
        parameters = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": date_from.strftime("%d/%m/%Y"),  # Search from tomorrow!
            "date_to": date_to.strftime("%d/%m/%Y"),  # Up to 6 months from today!
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "curr": self.curr,
            "one_for_city": 1,
            "max_stopovers": 0,  # You can change it to 0 if you want direct flights!
            "limit": 2,  # Returns only the cheapest option
        }

        try:
            response = requests.get(
                url=search_url, headers=self.headers, params=parameters
            )
            response.raise_for_status()  # Check for HTTPError
            data = response.json()
            if "data" in data and len(data["data"]) > 0:
                return data
            elif (
                "data" in data
                and len(data["data"]) == 0
                and parameters["max_stopovers"] == 0
            ):
                parameters["max_stopovers"] = 1
                response = requests.get(
                    url=search_url, headers=self.headers, params=parameters
                )
                print(f"No flights found for {destination_city_code}.")
                response.raise_for_status()  # Check for HTTPError
                data = response.json()
                if "data" in data and len(data["data"]) > 0:
                    return data
                else:
                    print(
                        f"No flights found for {destination_city_code} with 0 or 1 stopover. At the price you have set!"
                    )
                    return None
            else:
                print(
                    f"No flights found for {destination_city_code} with 0 or 1 stopover. At the price you have set!"
                )
                return None

        except HTTPError:
            print(f"HTTP error occurred: {response.status_code} - {response.reason}")
            return None
        except RequestException:
            print("A request error occurred.")
            return None
        except json.JSONDecodeError:
            print("Invalid JSON in response.")
            return None
        except KeyError:
            print(f"Unexpected data format from API for {destination_city_code}.")
            return None
