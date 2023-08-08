import os
import logging

import json

import openai
import spotipy


ENABLE_DEBUG = True

# GUI
APP_TITLE = "Voice Assistant"
MIN_WIDTH = 450
MIN_HEIGHT = 450

ICON_PATH = 'assets/icon.ico'

# Logging
# TODO fix logging settings to show only one source logs
if ENABLE_DEBUG:
    logging.basicConfig(level=logging.DEBUG)
else:
    logging.basicConfig(level=logging.WARNING)

# OpenaAI
# TODO add openai settings
OPENAI_MODEL = "gpt-3.5-turbo-0613"
with open("api_keys/openai_api_key", "r") as file:
    openai_api_key = file.read().strip()
    os.environ["OPENAI_API_KEY"] = openai_api_key
openai.api_key = os.environ['OPENAI_API_KEY']

# Spotify
# TODO change the way of setting up spotify client
SPOTIFY_USERNAME = "Hikami"
REDIRECT_URI = "http://google.com/callback/"
with open("api_keys/spotify_api_key.json", "r") as file:
    keys = json.load(file)
    CLIENT_ID = keys["client_id"]
    CLIENT_SECRET = keys["client_secret"]

spotify_oauth = spotipy.SpotifyOAuth(CLIENT_ID, CLIENT_SECRET, REDIRECT_URI)
token_dict = spotify_oauth.get_access_token()
SPOTIFY_TOKEN = token_dict['access_token']
