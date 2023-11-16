import data_manager as dm
from flight_data import FlightData as fd
from flight_search import FlightSearch as fs
from notification_manager import NotificationManager 

# We get the flights that we have in our list! Keep in mind the free tier is up to 200 requests per month!!!! SO DO NOT DO TOO MANY TESTS :P
destinations = dm.DataManager()
email_list = [""]

alerts = NotificationManager()
offers = []

for flight in destinations.current_destinations:
    search = fs(flight['iataCode'])
    results = fd(search)
    
    if flight['price'] >= results.price:
        offer_text = results.flight_details()
        offers.append(offer_text)
        alerts.send_sms(offer_text)
        
for email in email_list:
    alerts.send_email(receiver_email=email, offers=offers)

