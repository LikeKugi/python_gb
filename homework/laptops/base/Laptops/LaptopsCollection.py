import pickle

from .Laptop import Laptop


class LaptopsCollection:
    PATH = 'data/laptops_collection.bin'

    def __init__(self):
        self.laptops = set()
        self.price = set()
        self.screen = set()
        self.ram = set()
        self._cpu = set()
        self.storage = set()

    def add(self, other: Laptop):
        if type(other) != Laptop:
            raise TypeError(f'{other} should be type of Laptop')

        self.laptops.add(other)

        self.price.add(other.price)
        self._cpu.add(other.cpu)
        self.ram.add(other.ram)
        self.storage.add(other.storage)
        self.screen.add(other.screen)

    def filter(self, prop, min_value=None):
        if min_value:
            sort_list = filter(lambda x: x[prop] >= min_value, self.laptops)
        else:
            sort_list = self.laptops

        out_list = sorted(sort_list, key=lambda x: (x[prop], x['product_name']))
        return out_list

    def dump(self):
        with open(self.PATH, 'wb') as ouf:
            pickle.dump(self, ouf)
