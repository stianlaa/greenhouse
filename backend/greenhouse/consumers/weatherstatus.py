"""
weatherstatus.py
- offers consumer methods towards weather api, with appropriate mapping 
"""

import requests
from bs4 import BeautifulSoup as Soup
from greenhouse.data.storage import store_weatherdata

# lat = 59.91
# lon = 10.63
# msl = 33
# https://api.met.no/weatherapi/nowcast/0.9/ # only offers precipitation 

base_url = "https://api.met.no/weatherapi/locationforecast/1.9/" #large forecast url
params = {'lat': '59.91', 'lon': '10.63'}

def fetch_and_store_weatherdata(conn):
    res = requests.get(base_url, params=params, timeout=7)
    soup = Soup(res.text,"xml")
    print(soup.time["from"])
    print(soup.time.location.temperature["value"])
    store_weatherdata(conn, (soup.time["from"], soup.time.location.temperature["value"], soup.time.location.humidity["value"], soup.time.location.cloudiness["percent"]))

def just_fetch_weatherdata():
    res = requests.get(base_url, params=params, timeout=7)
    soup = Soup(res.text,"xml")
    return {'from': soup.time["from"], 'temperature': soup.time.location.temperature["value"], 'humidity': soup.time.location.humidity["value"], 'cloudiness': soup.time.location.cloudiness["percent"]}

    #  invalid_msg = {
#             'message': 'Invalid token. Registeration and / or authentication required',
#             'authenticated': False
#         }