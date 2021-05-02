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
    for key, value in parsed_data:
        if pattern.match(key) or pattern.match(value):
            return_list.append({"key": key, "value": value})
    return return_list
