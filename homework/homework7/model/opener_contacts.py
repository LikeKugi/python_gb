import os
import pickle


def open_contacts():
    if os.stat('contacts.bin').st_size > 0:
        with open('contacts.bin', 'rb') as inf:
            db_contacts = pickle.load(inf)
        return db_contacts
    else:
        return dict()
