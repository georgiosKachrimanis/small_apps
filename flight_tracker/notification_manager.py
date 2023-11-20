
from twilio.rest import Client
import os
import smtplib
import os
from email.message import EmailMessage


class NotificationManager:
    """
    Manages the sending of notifications through SMS and email.

    Attributes:
        account_sid (str): Your Twilio account SID.
        auth_token (str): Your Twilio authentication token.
        twilio_number (str): Your Twilio phone number.
        my_number (str): The phone number to which SMS notifications will be sent.
        email (str): The email address used for sending notifications.
        email_key (str): The password or API key for the email account.
        email_smtp_server (str): The SMTP server for the email account.
        client (Client): Twilio client for sending SMS.

    Methods:
        send_sms(flight_information): Sends an SMS with the flight information.
        send_email(receiver_email, offers): Sends an email to a receiver with a list of offers.
    """ 
    
    def __init__(self) -> None:
        self.account_sid = os.environ['TWILIO_ACCOUNT_SID']
        self.auth_token = os.environ['TWILIO_AUTH_TOKEN']
        self.twilio_number = os.environ['TWILIO_NUMBER']
        self.my_number = os.environ['MY_NUMBER']
        self.email = os.environ['MY_SECOND_EMAIL']
        self.email_key = os.environ['MY_SECOND_EMAIL_KEY']
        self.email_smtp_server = os.environ['MY_SMTP_SERVER']
        self.client = Client(self.account_sid, self.auth_token)
       
        
    def send_sms(self, flight_information:str):
        message = self.client.messages.create(
            body=flight_information,
            from_=self.twilio_number,
            to=self.my_number
        )
        print(message.status)
        
    def send_email(self, receiver_email:str, offers:list):
        email_body = "\n".join(offers)
        message = EmailMessage()
        message['Subject' ]= "Todays flight deals!"
        message['From'] = self.email
        message['To'] = receiver_email
        message.set_content(email_body)
        
        with smtplib.SMTP(self.email_smtp_server, port=587) as connection:
            connection.starttls()  # Secure the connection with TLS
            connection.login(user=self.email, password=self.email_key)
            # Send the email with a randomized birthday letter.
            connection.send_message(message)
            