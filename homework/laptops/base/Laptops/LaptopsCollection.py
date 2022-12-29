import pickle

from .Laptop import Laptop


class LaptopsCollection:
    PATH = 'data/laptops_collection.bin'

    def __init__(self):
        self.laptops = set()
        self.prices = set()
        self.inches = set()
        self.rams = set()
        self.cpus = set()
        self.storages = set()

    def add(self, other: Laptop):
        if type(other) != Laptop:
            raise TypeError(f'{other} should be type of Laptop')

        self.laptops.add(other)

        self.prices.add(other.price)
        self.cpus.add(other.cpu)
        self.rams.add(other.ram)
        self.storages.add(other.storage)
        self.inches.add(other.screen)

    def filter(self, prop, min_value=None):
        if min_value:
            sort_list = filter(lambda x: x[prop] > min_value, self.laptops)
        else:
            sort_list = self.laptops

        out_list = sorted(sort_list, key=lambda x: (x[prop], x['product_name']))
        return out_list

    def dump(self):
        with open(self.PATH, 'wb') as ouf:
            pickle.dump(self, ouf)
