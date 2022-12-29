import pickle
import os

from .LaptopsCollection_create import create_collection_laptops

PATH = 'data/laptops_collection.bin'


def load_db():
    laptops = create_collection_laptops()
    save_laptops(laptops)
    return laptops


def get_laptops():
    """
    read database of laptops
    :return: set[LaptopsCollections]
        returns set of Laptops
    """
    with open(PATH, 'rb') as inf:
        laptops = pickle.load(inf)
        return laptops


def save_laptops(database) -> None:
    """
    Saves set to the file
    :param database: set[LaptopsCollections]
    :return: None
    """
    with open(PATH, 'wb') as ouf:
        pickle.dump(database, ouf)
