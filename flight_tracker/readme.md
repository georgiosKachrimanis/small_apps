# Flight Deal Finder

## Description
This application searches for flight deals and notifies subscribers of any new or better deals. It interacts with the Kiwi Flight Search API to find flight details and manages data using a Google Sheet or similar service.

## Features
- Searches for the best flight deals.
- Notifies users through SMS and email.
- Manages flight and user data with a remote data sheet.

## How to Use
1. Set environment variables for API keys and account credentials.
2. Run `main()` to start the flight deal search.
3. Use `add_user()` to add new users to the notification list.

## Dependencies
- `requests`: For API requests.
- `twilio`: For sending SMS.
- `smtplib` and `email`: For sending emails.

## Setup
### Prerequisites
1. **Python Installation:**
   Ensure that Python (preferably Python 3.6 or later) is installed on your system.

### Required Accounts and API Keys
1. **Kiwi API (Tequila):**
   - Sign up for an account at [Kiwi API](https://tequila.kiwi.com/portal/login/register) for flight search functionality.
   - Generate an API key from the Kiwi API portal.

2. **Twilio for SMS Notifications:**
   - Create an account on [Twilio](https://www.twilio.com/try-twilio).
   - Verify a phone number with Twilio to send SMS.
   - Obtain your Account SID and Auth Token from the Twilio console.
   - Get a Twilio phone number to send SMS.

3. **Google Sheets API (Optional):**
   - If using Google Sheets to manage data, enable the Google Sheets API from the [Google Developers Console](https://console.developers.google.com/).
   - Create a service account and download the credentials file.

4. **SMTP Email Service:**
   - Use an existing email service provider (like Gmail, Outlook, etc.) that supports SMTP.
   - Enable SMTP in your email account settings.
   - Obtain the SMTP server details and SMTP credentials (username and password/API key).

### Setting Up Environment Variables
Set the following environment variables in your system:

- `KIWI_KEY`: Your Kiwi API key.
- `TWILIO_ACCOUNT_SID`: Your Twilio Account SID.
- `TWILIO_AUTH_TOKEN`: Your Twilio Auth Token.
- `TWILIO_NUMBER`: Your Twilio phone number.
- `MY_NUMBER`: The phone number where SMS will be sent.
- `MY_SECOND_EMAIL`: Your email address for sending notifications.
- `MY_SECOND_EMAIL_KEY`: Your email's password or API key for SMTP.
- `MY_SMTP_SERVER`: The SMTP server address of your email provider.

## Contributing
For now I do not have any plans for contribution. If anyone wants to use this code feel free to do so!


## License

This project is licensed under the MIT License.

For the full text of the license, refer to the [MIT License](https://opensource.org/licenses/MIT).
