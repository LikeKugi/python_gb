import pickle

from contact import Contact


def open_file() -> dict[int, Contact]:
    with open('contacts.bin', 'rb') as inf:
        db_contacts = pickle.load(inf)
    return db_contacts


def output(db: dict[int, Contact]) -> None:
    for contact in db.values():
        print(contact)


def print_contacts() -> None:
    """
    print the contacts
    :return: None
    """
    data = open_file()
    output(data)