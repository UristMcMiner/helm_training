from config import load_env_config
import requests
config_data = load_env_config()


def hello_world():
    return 'Welcome to the RPi Home automation API'


def get_entries():
    endpoint = config_data['search_endpoint']
    params = {
        "regex": ".*"
    }
    response = requests.get("%s/api/v1.0/search" % endpoint, params=params)
    return response.json()
