import json

from .set_laptops import save_laptops
from .Laptop import Laptop

PATH = 'data/laptop_first.json'


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
    laptops_set = create_set_laptops()
    save_laptops(laptops_set)


def create_database(laptops: json):
    goods = set()
    for el in laptops:
        laptop = Laptop(*el.values())
        goods.add(laptop)
    return goods


def create_set_laptops():
    data = read_json()
    laptops = create_database(data)
    return laptops


if __name__ == '__main__':
    print(read_json())
