import data_manager as dm
from flight_data import FlightData as fd
from flight_search import FlightSearch as fs
from notification_manager import NotificationManager 
from datetime import datetime,timedelta

ORIGIN = 'AMS'

def main():
    # We get the flights that we have in our list! 
    
    flights = fs()
    database = dm.DataManager(flight_search=flights)

    alerts = NotificationManager()
    offers = []
    date_from = datetime.now() + timedelta(days=1)
    date_to = datetime.now() + timedelta(days=180)

    for flight in database.get_destinations():
        search = fs().check_available_flights(origin_city_code=ORIGIN, destination_city_code=flight['iataCode'],date_from=date_from, date_to=date_to )
        
        # In Case we do not have any flights to the location
        if search is None:
            continue
        
        results = fd(search)
        
        if flight['price'] >= results.price:
            offer_text = results.flight_details()
            offers.append(offer_text)
            # If you want to send sms(I have a trial account so do not want to spend my free tier on 3-4 texts per time I run this), uncomment the next lien!
            # alerts.send_sms(offer_text)
            
    for email in database.get_email_list():
        alerts.send_email(receiver_email=email['Email'], offers=offers)


if __name__ == "__main__":
    main()
