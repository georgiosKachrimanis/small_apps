import smtplib
import datetime as dt
from random import randint
import pandas as pd
import os

# Determine the base directory of this script to make file paths relative to the script location.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Construct paths to the birthday CSV file and the letter templates using the base directory.
BIRTHDAY_FILE = os.path.join(BASE_DIR, "birthdays.csv")
LETTERS_LOCATION = os.path.join(BASE_DIR, "letter_templates", "letter_")

# Email credentials and SMTP server configuration.
MY_EMAIL = "your email goes here"
# The smtp service providers can create an one time password to use to lod in the email API. 
# You can find more information with some google search!
MY_PASSWORD = "the password you will get from your provider goes here!"  
# Depending on the email service you are using you must change this!
MY_SMTP_SERVER = "smtp.gmail.com"  

# Email subject line for the birthday message.
SUBJECT = "Subject:Happy Birthday!\n\n"


def email_app(name: str, email: str):
    """Sends a birthday email to the specified recipient.

    Args:
        name: Name of the email recipient.
        email: Email address of the recipient.
    """
    with smtplib.SMTP(MY_SMTP_SERVER, port=587) as connection:
        connection.starttls()  # Secure the connection with TLS
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        # Send the email with a randomized birthday letter.
        connection.sendmail(
            from_addr=MY_EMAIL, to_addrs=email, msg=f"{SUBJECT}{random_letter(name)}"
        )


def random_letter(name: str):
    """Generates a personalized birthday letter for the recipient.

    Args:
        name: Name of the recipient to personalize the letter.

    Returns:
        A string with the personalized letter.
    """
    # Randomly select a letter template.
    file_name = f"{LETTERS_LOCATION}{randint(1,3)}.txt"

    # Open and read the selected letter template.
    with open(file_name, "r") as chosen_letter:
        letter_content = chosen_letter.read()

    # Replace the placeholder with the recipient's name.
    letter = letter_content.replace("[NAME]", name)

    return letter


# Get the current date to check against the birthday list.
today = dt.datetime.now()

# Load the birthday data from CSV into a DataFrame.
try:
    df = pd.read_csv(BIRTHDAY_FILE)
except FileNotFoundError as e:
    # Handle the error if the file is not found.
    print(f"There was a problem: {e}")

# Iterate over the DataFrame to check for birthdays today.
for index, row in df.iterrows():
    # Check if the current day and month match a birthday in the list.
    if row["month"] == today.month and row["day"] == today.day:
        # Send an email to users who have a birthday today.
        email_app(row["name"], row["email"])
