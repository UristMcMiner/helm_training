from config import cache_file
import json
import re


def hello_world():
    return 'Welcome to the RPi Home automation API'


def search(regex_str):
    cache_handle = open(cache_file)
    parsed_data = json.loads(cache_handle.read())
    pattern = re.compile(regex_str)
    return_list = list()
    for key in parsed_data.keys():
        data = parsed_data[key]
        if pattern.match(key) or pattern.match(data):
            return_list.append({"key": key, "value": data})
    return return_list
