import os

import requests
import spotipy
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()
header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:142.0) Gecko/20100101 Firefox/142.0"
}

id = os.getenv("CLIENT_ID")
secret = os.getenv("CLIENT_SECRET")
uri = os.getenv("REDIRECT_URI")

date_to_visit = input(
    "Year do you want to travel to? Type the date in this format YYYY-NN-DD:"
)
year = date_to_visit.split("-")[0]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        client_id=id,
        client_secret=secret,
        redirect_uri=uri,
        cache_path="./token.txt",
    )
)

me = sp.current_user()["id"]

# NOTE: creating the playlist
playlist = sp.user_playlist_create(
    user=me, name=f"Nostalgia playlist from {date_to_visit}", public=False
)
playlist_id = playlist["id"]

url = f"https://www.billboard.com/charts/hot-100/{date_to_visit}/"

response = requests.get(url=url, headers=header)
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")
all_titles = soup.select("li ul li h3")
titles = [i.get_text(strip=True) for i in all_titles]

# NOTE: adding songs to playlist
for song_name in titles:
    result = sp.search(q=f"track:{song_name} year:{year}", type="track", limit=1)

    if result["tracks"]["items"]:
        track_id = result["tracks"]["items"][0]["id"]
        sp.playlist_add_items(playlist_id, [track_id])

    else:
        continue
