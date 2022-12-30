import os
from dotenv import load_dotenv, find_dotenv


class Settings:
    load_dotenv(find_dotenv('settings.env'))

    api_key = os.environ.get('APIKEY')


settings = Settings()

