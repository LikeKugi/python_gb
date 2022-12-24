import json
import pickle

from Laptop import Laptop


def read_json() -> json:
    with open("../data/laptop.json") as inf:
        laptops = json.load(inf)
        return laptops


def create_database(laptops: json):
    goods = set()
    for el in laptops:
        laptop = Laptop(*el.values())
        print(laptop)
        goods.add(laptop)
    return goods


def save_info(database: set) -> None:
    with open('laptops_set.bin', 'wb') as ouf:
        pickle.dump(database, ouf)


if __name__ == '__main__':
    data = read_json()
    create_database(data)
