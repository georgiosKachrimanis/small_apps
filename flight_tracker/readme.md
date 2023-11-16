# Flight Deals Finder

## Overview
This project is a flight deals finder, which helps users to find the best flight deals. It interacts with various APIs to fetch flight data, manage notifications, and keep track of destinations.

## Classes

1. **DataManager**: Handles communication with the Google Sheet containing flight deal information.

2. **FlightData**: Structures the flight data obtained from the Flight Search API.

3. **FlightSearch**: Interacts with the Flight Search API to find flight details.

4. **NotificationManager**: Sends notifications with flight deal details via SMS and email.

## Features
- Fetch and store current flight destinations.
- Search for flights and obtain detailed information.
- Send alerts about flight deals through SMS and email.

## Usage
To use this project, set up the required environment variables for API access and configure the destination details in the Google Sheet.

## Dependencies
- Twilio
- Requests

## Author
G.Kachrimanis

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.