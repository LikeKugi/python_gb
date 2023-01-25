import os
import json

PATH = 'storage/klasses.json'


def open_json(path=PATH) -> json:
    if not (os.path.exists(path) and os.path.getsize(path) > 0):
        raise FileNotFoundError
    with open(path) as inf:
        data = json.load(inf)
    return data


def create_json(new_data: dict, path=PATH):
    data = open_json(path)
    data.append(new_data)

    with open(path, 'w') as ouf:
        json.dump(data, ouf)
