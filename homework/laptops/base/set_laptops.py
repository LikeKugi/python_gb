import pickle

PATH = 'laptops_set.bin'


def get_laptops() -> set:
    """
    read database of laptops
    :return: set[Laptop]
        returns set of Laptops
    """
    with open(PATH, 'rb') as inf:
        laptops = pickle.load(inf)
        return laptops


def save_laptops(database: set) -> None:
    """
    Saves set to the file
    :param database: set[Laptop]
    :return: None
    """
    with open(PATH, 'wb') as ouf:
        pickle.dump(database, ouf)
