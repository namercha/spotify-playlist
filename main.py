import requests
from bs4 import BeautifulSoup
import os
import spotipy
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()
SPOTIPY_CLIENT_ID = os.environ["SPOTIFY_CLIENT_ID"]
SPOTIPY_CLIENT_SECRET = os.environ["SPOTIFY_CLIENT_SECRET"]

date = input("What year do you want to travel to? Type the date in the formal YYYY-MM-DD: ")
URL = "https://www.billboard.com/charts/hot-100/" + date + "/"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

all_songs = soup.find_all(name="div", class_="o-chart-results-list-row-container")
songs = [song.find(name="h3", id="title-of-a-story").getText().strip() for song in all_songs]
print(songs)

# Authenticate with Spotify
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
    )
)
user_id = sp.current_user()["id"]
print(user_id)
