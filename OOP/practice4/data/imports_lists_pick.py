import os
import pickle

PATH = 'storage/students.bin'


def read_file(path=PATH):
    if not (os.path.exists(path) and os.path.getsize(path) > 0):
        raise FileNotFoundError
    with open(path, 'rb') as inf:
        data = pickle.load(inf)
    return data


def create_file(data, path=PATH):
    with open(path, 'wb') as ouf:
        pickle.dump(data, ouf)
