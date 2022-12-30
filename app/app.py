from flask import Flask
import requests
from core.settings import settings


app = Flask(__name__)


# Home page contains form to let users ask input their postcode and if they want their door number
# Take that information and make a request to the address API and get the users lon and lat
# Maybe figure out a way to ask for their current location and use that?
@app.get('/')
def home():
    return '<h1>Hello World</h1>'


@app.route('/get_weather')
def get_weather_details():
    x = requests.get(f'https://api.openweathermap.org/data/2.5/forecast?lat=44.34&lon=10.99&appid={settings.weather_api_key}')
    print(x.json())
    return x.json()


@app.route('/address_lookup')
def get_address_json():
    # Returns a json object that gives the users address and lon and lat values, uses a postcode and door number
    x = requests.get(f'https://api.getAddress.io/find/nw21qd/45?api-key={settings.address_api_key}')

    # Returns a json object that gives
    y = requests.get(f'https://api.getAddress.io/find/nw118tn?api-key={settings.address_api_key}')
    return x.json()