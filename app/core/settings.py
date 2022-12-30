import os
from dotenv import load_dotenv, find_dotenv


class Settings:
    load_dotenv(find_dotenv('settings.env'))

    weather_api_key = os.environ.get('Weather_APIKEY')
    address_api_key = os.environ.get('Address_APIKEY')


settings = Settings()


