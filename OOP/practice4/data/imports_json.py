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
    jsoned = {i: s.toJSON() for i, s in new_data.items()}
    with open(path, 'w') as ouf:
        json.dump(jsoned, ouf)


def update_json(new_data: dict, path=PATH):
    try:
        data = open_json(path)
    except FileNotFoundError:
        data = {}
    data.update(new_data)
    create_json(data)
