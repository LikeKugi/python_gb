import pickle

from contact import Contact


def open_file() -> dict[int, Contact]:
    with open('contacts.bin', 'rb') as inf:
        db_contacts = pickle.load(inf)
    return db_contacts


def search_contact(db_contacts: dict[int, Contact], query: str) -> tuple[int, Contact] | None:
    query = query.lower()
    for index, val in db_contacts.items():
        if query in val.name or query in val.phone_number.replace('-', ''):
            return index, val
    else:
        return None


def search(query: str) -> tuple[int, Contact] | None:
    """
    search contact in db
    :param query: str
        name or phone
    :return: tuple[int, Contact] | None
         int - index of contact
         Contact - the contact in db
         None if no contact
    """
    db = open_file()
    if q := search_contact(db, query):
        return q
    else:
        return None


def is_contact(query: str) -> bool:
    """
    check if contact is in db
    :param query: name
    :return: bool
        True - is in
        False - not found
    """
    db = open_file()
    if search_contact(db, query):
        return True
    else:
        return False
