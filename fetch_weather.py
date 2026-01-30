import requests
from config import API_KEY,API_URL


def fetch_weather(city_name):
    payload={'key':API_KEY,'q':city_name}

    response=requests.get(API_URL,params=payload)

    response.raise_for_status()

    json_data=response.json()


    return json_data
