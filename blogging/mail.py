import smtplib
import os


# Email credentials and SMTP server configuration.
MY_EMAIL = os.environ.get("MY_MAIN_EMAIL")
MY_SECOND_EMAIL = os.environ.get("MY_SECOND_EMAIL")
MY_PASSWORD = os.environ.get("MY_SECOND_EMAIL_KEY")
MY_SMTP_SERVER = os.environ.get("MY_SMTP_SERVER")

# Email subject line for the birthday message.
SUBJECT = "Subject:You got a new message!\n\n"


class Mail:
    def __init__(self, name, email, phone, message) -> None:
        self.name = name
        self.email = email
        self.phone = phone
        self.message = message

    def email_message_formatter(self):
        email_message = f"Name: {self.name}\nEmail: {self.email}\nPhone number: {self.phone}\nMessage: {self.message}"
        return email_message

    def send_email(self):
        with smtplib.SMTP(MY_SMTP_SERVER, port=587) as connection:
            connection.starttls()  # Secure the connection with TLS
            connection.login(user=MY_SECOND_EMAIL, password=MY_PASSWORD)

            connection.sendmail(
                from_addr=MY_SECOND_EMAIL,
                to_addrs=MY_EMAIL,
                msg=f"{SUBJECT}{self.email_message_formatter()}",
            )
