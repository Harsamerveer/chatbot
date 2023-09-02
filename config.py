import os
from decouple import config

# Access the API key
api_key2 = config('API_KEY')

api_key = os.environ.get("API_KEY")

class Config(object):
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    OPENAI_KEY = api_key

config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}