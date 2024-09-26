import pandas as pd
import numpy as np
import requests
import os
import json


# extract the all the cities from the cities_list which can be used for extracting data
city_data = pd.read_excel('cities_list.xlsx')
cities = list(city_data['name'])


# extracting the raw data from OpenWeathermap, storing the json format
def cities_fetch_data(api_key,cities):
  weather_data = []
  #base_url = f"http://api.openweathermap.org/data/2.5/weather?"

  for city in cities:
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    result = requests.get(url)
    weather_data.append(result.json())

  return weather_data


key = "8a96d8609c56a83bea0de418f4d3d382"
weather_information = cities_fetch_data(key,cities)


with open('weather_data.json', 'w') as f:
    json.dump(weather_information, f)
