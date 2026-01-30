import requests
import logging
from config import API_KEY,API_URL
from requests.exceptions import ConnectionError,Timeout
from logger_func import setup_logger

def fetch_weather(city_name):
    payload={'key':API_KEY,'q':city_name}
    setup_logger()
    try :

        response=requests.get(API_URL,params=payload,timeout=10)
        response.raise_for_status()
        json_data=response.json()
        return json_data
    except ConnectionError:
        print("NO Network connection")
        logging.error("Network connection Error")
        return None

    except Timeout :
        print("Network is too slow")
        logging.error("Slow Network Error")
        return None

    except requests.exceptions.HTTPError as e :
        print("404 Error: ",e)
        return None
        
