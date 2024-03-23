import os
import logging
from logging import Logger

import json

import openai
import spotipy

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow


ENABLE_DEBUG = False

# GUI
APP_TITLE = "Voice Assistant"
MIN_WIDTH = 450
MIN_HEIGHT = 450

ICON_PATH = 'assets/icon.ico'

# Logging
# TODO fix logging settings to show only one source logs
level = logging.DEBUG if ENABLE_DEBUG else logging.INFO
logging.basicConfig(level=level)

# OpenaAI
# TODO add openai settings
OPENAI_MODEL = "gpt-3.5-turbo-0613"
with open("api_keys/openai_api_key.json", "r") as file:
    openai_api_key = file.read().strip()
    os.environ["OPENAI_API_KEY"] = openai_api_key
openai.api_key = os.environ['OPENAI_API_KEY']

# Spotify
# TODO change the way of setting up spotify client
SPOTIFY_REDIRECT_URI = "http://google.com/callback/"
with open("api_keys/spotify_api_key.json", "r") as file:
    keys = json.load(file)
    SPOTIFY_CLIENT_ID = keys["client_id"]
    SPOTIFY_CLIENT_SECRET = keys["client_secret"]

# Google APIs
# scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]
#
# # Set up OAuth 2.0 flow
# flow = InstalledAppFlow.from_client_secrets_file("api_keys/google_api_key.json", scopes)
# credentials = flow.run_local_server()
#
# # Youtube
# api_service_name = "youtube"
# youtube = build(api_service_name, api_version, credentials=credentials)
# api_version = "v3"

# Programs
AVAILABLE_PROGRAMS = {
    'League of Legends': {
        "executable": r"",
        "parameters": {
            "launch-product": "league_of_legends",
            "launch-patchline": "live",
        }
    },
    'Discord': {
        "executable": r"",
        "parameters": {
            "processStart": "Discord.exe",
        },
    },
    'Spotify': {
        "executable": r"",
        "parameters": {}
    }
}