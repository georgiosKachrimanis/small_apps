# Birthday Email Sender

A simple Python application to automatically send birthday wishes via email to individuals whose birthdays are listed in a CSV file.

## Features

- Loads a list of birthdays from a CSV file.
- Checks daily for any birthdays that match the current date.
- Sends a personalized birthday greeting via email.
- Uses randomized letter templates for sending wishes.

## Prerequisites

Before you run this application, you will need:

- Python 3 installed on your system.
- Access to an SMTP server and the credentials for sending emails.
- A CSV file containing the birthday information. For your convenience I have created an example CSV and you can just new lines with each new birthday. 

## Installation

1. Clone this repository to your local machine using `git clone`.
2. Install the required dependencies by running `pip install pandas`.
3. Configure your SMTP settings and email credentials in the script.

## Configuration

To configure the application, you will need to set the following:

- `MY_EMAIL`: Your email address from which the birthday emails will be sent.
- `MY_PASSWORD`: The password or application-specific password for your email account.
- `MY_SMTP_SERVER`: The SMTP server through which the emails will be sent.
- `BIRTHDAY_FILE`: The path to the CSV file containing the birthday data.

## Usage

To run the script, execute the following command:

`python3 biemsend.py`

## Extra notes

You can also run this from an online service like [pythonanywhere](https://www.pythonanywhere.com/).
The code is already optimized for this you only need to provide your logins and then add a Task to check daily for the birthdays.


