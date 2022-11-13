import pickle

from .contact import Contact


def _open_file() -> dict[int, Contact]:
    with open('contacts.bin', 'rb') as inf:
        db_contacts = pickle.load(inf)
    return db_contacts


def _output(db: dict[int, Contact]) -> None:
    for contact in db.values():
        print(contact)


def print_contacts() -> None:
    """
    print the contacts
    :return: None
    """
    data = _open_file()
    _output(data)