import random
import string
import json

cache_path = "/cache"

cache_size = 5000

cache_dict = {}

random_file = open("%s/random" % cache_path, 'w')

letters = string.ascii_lowercase


for i in range(0, cache_size):
    key = ''.join(random.choice(letters) for j in range(20))
    value = ''.join(random.choice(letters) for j in range(40))
    cache_dict[key] = value

random_file.write(json.dumps(cache_dict))
random_file.flush()
random_file.close()

