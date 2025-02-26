import os

from flask import Flask

from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
from spotipy.cache_handler import FlaskSessionCacheHandler

app = Flask("__name__")
app.config['SECRET_KEY'] = os.urandom(64)

client_id = 'e3ebd892691a4853bc0a34aac11e852a'
client_secret = 'a007d43223ac4b27b6d40fb4f05a9fb4'
redirect_uri = 'http://localhost:5000/callback'
scope = 'playlist-read-private'

if __name__ == '__main__':
    app.run(debug=True)

