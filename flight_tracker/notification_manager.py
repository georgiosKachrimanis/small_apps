
from twilio.rest import Client
import os
import smtplib
import os
from email.message import EmailMessage


class NotificationManager:
    """
    This class is responsible for sending notifications with flight deal details via SMS and email.

    Attributes:
        account_sid (str): Account SID for Twilio.
        auth_token (str): Authentication token for Twilio.
        twilio_number (str): Twilio phone number for sending SMS.
        my_number (str): Recipient phone number for SMS.
        email (str): Sender email address.
        email_key (str): Key for email server authentication.
        email_smtp_server (str): SMTP server for email.
        client (Client): Twilio client object.

    Methods:
        send_sms: Sends an SMS with the flight information.
        send_email: Sends an email with a list of flight offers.
    """
    def __init__(self) -> None:
        self.account_sid = os.environ['TWILIO_ACCOUNT_SID']
        self.auth_token = os.environ['TWILIO_AUTH_TOKEN']
        self.twilio_number = os.environ['TWILIO_NUMBER']
        self.my_number = os.environ['MY_NUMBER']
        self.email = 'georgios.k.kachrimanis@gmail.com'
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
            