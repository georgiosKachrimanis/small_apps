import requests
import os
from datetime import datetime


ENDPOINT_EXERCISE = "https://trackapi.nutritionix.com/v2/natural/exercise"
# Do not forget to authenticate sheety with google
ENDPOINT_SHEETY = "The LINK to your google sheet here."  

GENDER = ""
AGE = None
WEIGHT = None
HEIGHT = None

nutrionix_api_key = os.environ.get("NUTRIONIX_KEY")
nutrionix_id = os.environ.get("NUTRIONIX_ID")
sheety_user = os.environ.get("SHEETY_USER")
sheety_pass = os.environ.get("SHEETY_PASS")


nutrionix_headers = {"x-app-id": nutrionix_id, "x-app-key": nutrionix_api_key}
user_input = input("Tell me what exercise you did: \n")

nutrionix_params = {
    "query": user_input,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE,
}

response_nutrionix_api = requests.post(
    ENDPOINT_EXERCISE, json=nutrionix_params, headers=nutrionix_headers
)
response_nutrionix_api.raise_for_status()
result_nutrionix = response_nutrionix_api.json()
data_nutrionix = result_nutrionix["exercises"]


date = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime("%H:%M:%S")

for exercise in data_nutrionix:
    sheety_params = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    response_sheety_api = requests.post(
        ENDPOINT_SHEETY, json=sheety_params, auth=(sheety_user, sheety_pass)
    )
    response_sheety_api.raise_for_status()
    result_sheety = response_sheety_api.json()
    print(result_sheety)
