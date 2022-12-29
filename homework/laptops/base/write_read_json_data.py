import json
from .Laptops import save_laptops, create_collection_laptops

PATH = 'data/laptop.json'


def read_json() -> json:
    """
    reads json file
    :return: json
    """
    if __name__ == '__main__':
        path = f"..{PATH}"
    else:
        path = PATH
    with open(path) as inf:
        laptops = json.load(inf)
        return laptops


def write_json(new_laptop: dict) -> None:
    """
    write data to json file and update database of laptops
    :param new_laptop: dict
        the new laptop characteristics
    :return: None
    """
    data = read_json()
    data.append(new_laptop)
    with open(PATH, 'w') as ouf:
        json.dump(data, ouf)
