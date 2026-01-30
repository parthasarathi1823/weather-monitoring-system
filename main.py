import logging
from logger_func import setup_logger
from fetch_weather import fetch_weather
from parse_weather import climate_analyse
def main():
    setup_logger()
    try :
        city_name=input("Enter your City Name: ")
        data=fetch_weather(city_name)
        climate_analyse(data)
        logging.info(f"City :{city_name} Weather fetched ..")
        print("Weather data saved sucessfully ...")
    except Exception as e:
        logging.error(e) 
        print("Error:",e) 
        logging.error(e) 


main()
