import json

from .Laptop import Laptop

PATH = 'data/laptop.json'


def read_json() -> json:
    if __name__ == '__main__':
        path = "../data/laptop.json"
    else:
        path = PATH
    with open(path) as inf:
        laptops = json.load(inf)
        return laptops


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

