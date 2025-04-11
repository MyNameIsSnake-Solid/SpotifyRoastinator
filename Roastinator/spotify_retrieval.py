from flask import Flask, render_template  # type: ignore
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv # type: ignore
from spotipy.exceptions import SpotifyException
# from spotify.venv import load_dotenv
import os

load_dotenv()

CLIENT_ID = os.environ.get('CLIENT_KEY')
CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
REDIRECT_URI = 'http://localhost:5000'
cache_path = '.cache'

# will be called by the master file
def getData():
    print("Getting Data (WIP).")

    # check if the token cache is empty or corrupted. If so then delete it
    fixCache()

    # authenticate to be able to grab the data
    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            redirect_uri=REDIRECT_URI,
            scope='user-top-read',
        )
    )

    try:
        return pullFromSpotify(sp)
    except SpotifyException as e:
        if e.http_status == 401: # invalid token. AKA unauthorized
            print("invalid token")
            forceTokenRefresh(sp)
            return pullFromSpotify(sp)


    return pullFromSpotify(sp)

def forceTokenRefresh(sp):
    # Check if the cache file exists and remove it if it does (force refresh)
    if os.path.exists(cache_path):
        print("Cache file found. Deleting to force reauthentication.")
        os.remove(cache_path)

    sp.auth_manager = SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope='user-top-read'
    )

def pullFromSpotify(sp):
    top_artists = sp.current_user_top_artists(limit=5, time_range='long_term')
    top_songs = sp.current_user_top_tracks(limit=5, time_range='long_term')

    # for loops to get top 5 artists and songs
    artists = [f"{idx}. {artist['name']}" for idx, artist in enumerate(top_artists['items'], 1)]
    songs = [f"{idx}. {song['name']}" for idx, song in enumerate(top_songs['items'], 1)]

    # print("Gathered data:")
    # print(artists)
    # print(songs)

    #y

    return [artists, songs] # return an array that holds both arrays    

def fixCache():
    if os.path.exists(cache_path):
        with open(cache_path, 'r') as f:
            contents = f.read()
            if not contents.strip():
                print("Cache file is empty or corrupted, deleting it...")
                os.remove(cache_path)