import json
import requests
import webbrowser

import spotipy
from settings import SPOTIFY_TOKEN

spotifyObject = spotipy.Spotify(auth=SPOTIFY_TOKEN)


def get_current_weather(location):
    """
    Get the current weather in a given location.

    :param location: A name of the city, e.g. San Francisco, Boston
    :param unit: Unit of temperature - "celsius" or "fahrenheit"
    :return: Current weather information
    """

    url = "https://weatherapi-com.p.rapidapi.com/current.json"

    querystring = {
        'q': location,
    }

    headers = {
        "X-RapidAPI-Key": "4951643536msh1dde8875e19fd2fp14bccejsn045affb858b6",
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    return json.dumps(response.json())


# TODO finish the function. Remake return value. Add spotify desktop support.
def spotify_play_song(name):
    """
    Search a song by its name and play it in Spotify.

    :param name: A name of the song, e.g. Smells like teen spirit, Californication
    :return: True if the function worked.
    """
    search_result = spotifyObject.search(name, 1, 0, "track")
    songs_dict = search_result["tracks"]
    song_items = songs_dict['items']
    song = song_items[0]['external_urls']['spotify']
    webbrowser.open(song)
    return

