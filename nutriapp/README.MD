# Exercise Tracker Application

This application is designed to log your daily exercises using the Nutritionix API and record them in a Google Sheet through the Sheety API. It's a simple yet effective way to keep track of your fitness journey.

## Features

- Logs user exercise input.
- Uses the Nutritionix API to determine exercise specifics such as duration and calories burned.
- Records the exercise data into a Google Sheet using the Sheety API.

## Requirements

- Python 3
- Requests library
- Nutritionix API key
- Sheety API credentials

## Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/georgiosKachrimanis/small_apps.git
   cd nutriapp
   ```


2. Install dependencies :

    `pip install requests`

3. Set Environment Variables:
- You need to set up the following environment variables:
    - NUTRIONIX_KEY: Your Nutritionix API key.
    - NUTRIONIX_ID: Your Nutritionix App ID.
    - SHEETY_USER: Your Sheety username.
    - SHEETY_PASS: Your Sheety password.

4. Update your personal data:
    - GENDER
    - AGE
    - WEIGHT
    - HEIGHT

5. Create the google sheet you want to use and of course give sheety the rights to access the file.
6. Update the `ENDPOINT_SHEETY` with the new google sheet

7. Run Application:

## How to Use
- Run the script and input the exercise you did when prompted.
- The script will automatically log the exercise details including the date, time, name, duration, and calories burned into a Google Sheet.

## Contributing
Contributions, issues, and feature requests are welcome. 

## License
This project is licensed under the MIT License. 

## Contact

Project Link: https://github.com/georgiosKachrimanis/small_apps.git
