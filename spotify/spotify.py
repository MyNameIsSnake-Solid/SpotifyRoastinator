# do pip install for dotenv, flask, and spotipy

from flask import Flask, render_template, redirect, request, session, url_for
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os


# will be called by the master file
def getData():
    print("Getting Data (WIP)")

    load_dotenv()



    CLIENT_ID = os.environ.get('CLIENT_KEY')
    CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
    REDIRECT_URI = 'http://localhost:5000'


    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            redirect_uri=REDIRECT_URI,
            scope='user-top-read'
        )
    )


    top_artists = sp.current_user_top_artists(limit=5, time_range='long_term')
    top_songs = sp.current_user_top_tracks(limit=5, time_range='long_term')

    # for loops to get tge top 5 artists and songs
    artists = [f"{idx}. {artist['name']}" for idx, artist in enumerate(top_artists['items'], 1)]
    songs = [f"{idx}. {song['name']}" for idx, song in enumerate(top_songs['items'], 1)]


    #y

    print(artists)
    print(songs)