from flask import Flask, render_template, redirect, request, session, url_for  # type: ignore
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv # type: ignore
from spotipy.exceptions import SpotifyException
# from spotify.venv import load_dotenv
import os

load_dotenv()

CLIENT_ID = os.environ.get('CLIENT_KEY')
CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
REDIRECT_URI = 'http://localhost:5000/callback'
cache_path = '.cache'

# will be called by the master file
def getData(access_token):

    print("Getting Data (WIP).")

    # check if the token cache is empty or corrupted. If so then delete it

    # authenticate to be able to grab the data
    sp = spotipy.Spotify(auth=access_token)


    try:
        return pullFromSpotify(sp)
    except SpotifyException as e:
        raise

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

