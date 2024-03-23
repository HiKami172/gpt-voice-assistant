import json
import requests


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

