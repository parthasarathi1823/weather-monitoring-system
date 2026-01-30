import json




def climate_analyse(data):
    loc = data["location"]
    cur = data["current"]

    content = f"""
========= Weather Report =========
City        : {loc['name']}
Region      : {loc['region']}
Country     : {loc['country']}
Latitude    : {loc['lat']}
Longitude   : {loc['lon']}
Local Time  : {loc['localtime']}

Temperature : {cur['temp_c']} °C
Humidity    : {cur['humidity']} %
Condition   : {cur['condition']['text']}
Wind Speed  : {cur['wind_kph']} km/h
=================================
"""

    with open("output.txt", "a") as file:
        file.write(content + "\n")