from data import read_file

def load_data(path: str):
    try:
        students: list = read_file(path=path)
    except FileNotFoundError:
        students = []
    return students