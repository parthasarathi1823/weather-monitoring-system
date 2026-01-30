import requests
from config import API_KEY,API_URL

def fetch_weather() :
    payload={'key':API_KEY,'q':"Hyderabad"}

    response=requests.get(API_URL,params=payload)

    response.raise_for_status()

    json_data=response.json()


    return json_data
