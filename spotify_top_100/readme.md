# Billboard Hot 100 to Spotify Playlist

## Description
This application is designed to create a Spotify playlist based on the Billboard Hot 100 songs for a given date. It scrapes the Billboard Hot 100 website for song titles and searches for these songs on Spotify. If found, it adds them to a newly created private Spotify playlist.

## Requirements


Before running the script, ensure you have Python installed on your system. Then, install the required libraries using pip:

`pip install requests beautifulsoup4 spotipy` 


To run the script, execute it with Python:

`python top_100.py`

You will be prompted to enter a date in the format YYYY-MM-DD. The script will then scrape the Billboard Hot 100 for the given date, search for the songs on Spotify, and create a playlist.

### Spotify API Credentials

Spotify account.

Activate [Developer tools in Spotify](https://developer.spotify.com/)

The [spotipy library](https://spotipy.readthedocs.io/en/2.22.1/?highlight=playlist%5C#)

The script requires Spotify API credentials:

CLIENT_ID

CLIENT_SECRET

REDIRECT_URI

You must register your application with Spotify and insert your own credentials in the script. [Spotify Dashboard](https://developer.spotify.com/dashboard).

## Disclaimer
This script is for educational purposes only. Ensure you have permission to scrape any website and that your actions comply with the website's terms of service or usage policies. Also, adhere to Spotify's API usage guidelines.

