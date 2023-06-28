# Idk why but this seems like the easiest way to attempt using an API
# so we're going to do it 

# We need API Key from env.. but ENV is in diff folder?
import os

import datetime as dt

import requests # Use this to send requests to the API


BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = '9642da6a311982271840ac1c866071f6'
CITY = "Chicago"

url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY

TMP_URL = "http://api.openweathermap.org/data/2.5/forecast?id=524901&appid=" + API_KEY

# Testing Below

TEST_URL = "http://api.openweathermap.org/data/2.5/forecast?lat=44.34&lon=10.99&appid=9642da6a311982271840ac1c866071f6" 

response = requests.get(TEST_URL).json()

print(response)