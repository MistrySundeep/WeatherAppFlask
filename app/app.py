from flask import Flask
import requests

app = Flask(__name__)


@app.route('/')
def home():
    # potential way to do API call through flask, need to move API key out to config file and figure out how to generate lon and lat values
    x = requests.get('https://api.openweathermap.org/data/2.5/forecast?lat=44.34&lon=10.99&appid=3817714559fbf80828a3d735f703b97b')
    print(x.json())
    return x.json()
