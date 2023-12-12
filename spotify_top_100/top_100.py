from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os


# Billboard Hot 100 URL
TOP_100_URL = "https://www.billboard.com/charts/hot-100/"

# Spotify Auth
OAUTH_AUTHORIZE_URL = "https://accounts.spotify.com/authorize"
OAUTH_TOKEN_URL = "https://accounts.spotify.com/api/token"
CLIENT_ID = os.environ.get("SPOTIFY_ID")
CLIENT_SECRET = os.environ.get("SPOTIFY_SECRET")
REDIRECT_URI = "https://example.com"
USER_NAME = os.environ.get("SPOTIFY_USER_NAME")

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope="playlist-modify-private",
        username=USER_NAME,
        show_dialog=True,
    )
)

user_id = sp.current_user()["id"]


def spotify_search(title_list: list) -> list:
    """
    Searches Spotify for the provided song titles and returns a list of Spotify URIs.

    Parameters:
    title_list (list): A list of song titles to search on Spotify.

    Returns:
    list: A list of Spotify URIs corresponding to the found songs. If a song is not found on Spotify, it is skipped.
    """

    uri_list = []
    for title in title_list:
        try:
            search_results = sp.search(q=f"track:{title}", type="track", limit=1)
            uri_list.append(search_results["tracks"]["items"][0]["uri"])
        except IndexError:
            print(f"Song {title}, is not available is not available in spotify")
    return uri_list


def songs_list(date) -> list:
    """
    Fetches the list of top songs from the Billboard Hot 100 for a given date.

    Parameters:
    date (str): The date for which the Billboard Hot 100 list is to be fetched. The date should be in the format 'YYYY-MM-DD'.

    Returns:
    list: A list of song titles from the Billboard Hot 100 for the specified date.
    """

    response = requests.get(url=f"{TOP_100_URL}/{date}/")
    soup = BeautifulSoup(response.text, "html.parser")
    song_titles = soup.select("li ul li h3")

    titles = []

    for song in song_titles:
        titles.append(song.getText().strip())
    return titles


def create_playlist(songs_uri: list, date: str):
    """
    Creates a private Spotify playlist with the given song URIs and date in the playlist name.

    Parameters:
    songs_uri (list): A list of Spotify URIs to include in the playlist.
    date (str): The date which will be included in the name of the playlist.

    Returns:
    None: This function does not return any value.
    """

    playlist = sp.user_playlist_create(
        user=user_id, name=f"Top 100 songs of week: {date}", public=False
    )["id"]

    sp.playlist_add_items(playlist_id=playlist, items=songs_uri)


def main():
    date_input = input(
        "What date do you travel to?\nType the date in this format YYYY-MM-DD: "
    )

    songs_list_uri = spotify_search(songs_list(date=date_input))

    create_playlist(songs_uri=songs_list_uri, date=date_input)


if __name__ == "__main__":
    main()
