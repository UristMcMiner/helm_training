import os
def load_env_config():
    return_data = {
        "search_endpoint": os.environ['SEARCH_ENDPOINT']
    }
    return return_data