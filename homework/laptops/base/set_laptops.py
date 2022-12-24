import pickle


def get_laptops():
    with open('laptops_set.bin', 'rb') as inf:
        laptops = pickle.load(inf)
        return laptops


def save_laptops(database: set) -> None:
    with open('laptops_set.bin', 'wb') as ouf:
        pickle.dump(database, ouf)
