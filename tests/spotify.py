import json
import os

import spotipy
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyClientCredentials

load_dotenv()

client_id = os.environ.get("SPOTIFY_CLIENT_ID")
client_secret = os.environ.get("SPOTIFY_CLIENT_SECRET")

sp = spotipy.Spotify(
    auth_manager=SpotifyClientCredentials(
        client_id=client_id, client_secret=client_secret
    )
)

results = sp.search("Cold War Kids What you say", limit=1)

with open("spotipy.json", "w") as fp:
    json.dump(results, fp, indent=2)

print("id =", results["tracks"]["items"][0]["id"])
print("uri =", results["tracks"]["items"][0]["uri"])
