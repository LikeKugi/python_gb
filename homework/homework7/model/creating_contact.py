import pickle

from contact import Contact
from searching_contact import is_contact


def get_values() -> tuple[str | None, str | None]:
    value_name = input('Enter name: ')
    value_phone = input('Enter phone number: ')
    return value_name, value_phone


def add_contact(name: str | None, phone: str | None) -> Contact | None:
    if name:
        query = name
    else:
        query = phone
    if not is_contact(query):
        unit = Contact(name, phone)
        return unit
    return None


def add_to_file(contact: Contact) -> None:
    with open('contacts.bin', 'a+b') as ouf:
        try:
            db_contacts = pickle.load(ouf)
            position = len(db_contacts)
            db_contacts[position] = contact
        except Exception as e:
            with open('log.txt', 'a') as log_file:
                print(e, file=log_file)
        else:
            print('DONE')
        finally:
            pickle.dump(db_contacts, ouf)


def create() -> None:
    """
    create contact and add it to db
    :return: None
    """
    name, phone = get_values()
    contact = add_contact(name, phone)
    if contact:
        add_to_file(contact)
    else:
        print('Already exists')
