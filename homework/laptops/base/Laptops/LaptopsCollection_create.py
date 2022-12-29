import json

from .Laptop import Laptop
from .LaptopsCollection import LaptopsCollection

PATH = 'data/laptop.json'
PATH_COLLECTION = 'data/laptops_collection.bin'


def _read_json(path=PATH) -> json:
    """
    reads json file
    :return: json
    """
    with open(path) as inf:
        laptops = json.load(inf)
        return laptops


def _create_collection(laptops: json):
    goods = LaptopsCollection()
    for el in laptops:
        laptop = Laptop(*el.values())
        goods.add(laptop)
    return goods


def create_collection_laptops():
    """
    reads data from json and returns a collection of Laptops
    :return:
    """
    data = _read_json()
    laptops = _create_collection(data)
    return laptops

