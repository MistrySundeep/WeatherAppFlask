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


@app.route('/address_lookup')
def get_address_json():
    # Returns a json object that gives the users address and lon and lat values, uses a postcode and door number
    x = requests.get(f'https://api.getAddress.io/find/nw21qd/45?api-key={settings.address_api_key}')
    x_json = x.json()

    results = {
        'lat': x_json.get('latitude'),
        'lon': x_json.get('longitude')
    }
    # Returns a json object that gives the users address, lon and lat values using only a postcode
    # y = requests.get(f'https://api.getAddress.io/find/nw118tn?api-key={settings.address_api_key}')
    return results


# To add variable use <type:name> as seen below
@app.route('/get_weather/<string:postcode>')
def get_weather_details(postcode: str):
    # Format the postcode
    print(postcode.lower().replace(" ", ""))

    # Get address details
    address_coordinates = requests.get(f'https://api.getAddress.io/find/{postcode}?api-key={settings.address_api_key}').json()

    # Create a dict that will hold the lat and lon of the address
    coordinate_dict = {
        'lat': address_coordinates.get('latitude'),
        'lon': address_coordinates.get('longitude')
    }

    # Make a request for the weather of this location using the dict values
    # units=metric for degrees values
    # cnt=1 sets the number of records returned, default is 20?
    weather = requests.get(f'https://api.openweathermap.org/data/2.5/forecast?lat={coordinate_dict.get("lat")}&lon={coordinate_dict.get("lon")}&units=metric&cnt=1&appid={settings.weather_api_key}').json()
    print(weather)

    return weather
