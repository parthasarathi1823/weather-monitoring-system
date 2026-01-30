import json
from fetch_weather import fetch_weather



def Climate_analyse():
    data=fetch_weather()
    loc=data['location']
    cur=data['current']

    with open("output.txt","w") as file:

        file.write("======= {} Weather details =======\n\n".format("Hyderabad"))
        file.write("\t\tCity Name          : {}\n".format(loc['name']))
        file.write("\t\tRegion             : {}\n".format(loc['region']))
        file.write("\t\tCountry            : {}\n".format(loc['country']))
        file.write("\t\tLatitude           : {}\n".format(loc['lat']))
        file.write("\t\tLongitude          : {}\n".format(loc['lon']))
        file.write("\t\tPresent Time       : {}\n".format(loc['localtime']))
        file.write("\t\tUV                 : {}\n".format(cur["uv"]))
        file.write("\t\tHumidity           : {}\n".format(cur["humidity"]))
        file.write("\t\tClouds             : {}\n".format(cur["cloud"]))
        file.write("\t\tCondition          : {}\n".format(cur['condition']['text']))
        file.write("\t\tTemperature (in c) : {}\n".format(cur['temp_c']))
        file.write("\t\tWind speed (mph)   : {}\n".format(cur['wind_mph']))
        
Climate_analyse()       
