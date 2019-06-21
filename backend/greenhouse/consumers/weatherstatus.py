"""
weatherstatus.py
- offers consumer methods towards weather api, with appropriate mapping 
"""

import requests
from bs4 import BeautifulSoup as Soup
from greenhouse.data.storage import add_weatherdata

# lat = 59.91
# lon = 10.63
# msl = 33
# https://api.met.no/weatherapi/locationforecast/1.9/

def fetch_and_store_weatherdata(conn):
    base_url = "https://api.met.no/weatherapi/locationforecast/1.9/" # large forecast
    # base_url = "https://api.met.no/weatherapi/nowcast/0.9/" # only offers precipitation 

    params = {'lat': '59.91', 'lon': '10.63'}

    res = requests.get(base_url, params=params, timeout=7)
    soup = Soup(res.text,"xml")
    soup_result = soup.find("time").find("location")

    add_weatherdata(conn, (soup.time["from"], soup.time.location.temperature["value"], soup.time.location.humidity["value"], soup.time.location.cloudiness["percent"]))
