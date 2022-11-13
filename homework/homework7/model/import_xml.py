import pickle
from xml.etree import ElementTree

from .contact import Contact


def _open_file() -> dict[int, Contact]:
    with open('contacts.bin', 'rb') as inf:
        db_contacts = pickle.load(inf)
    return db_contacts


def _write_file_xml(data: dict[int, Contact]) -> None:
    root = ElementTree.Element('Addressbook')

    for index, contact in data.items():
        count = ElementTree.SubElement(root, f'contact {index}')

        c_name = ElementTree.SubElement(count, 'Name')
        c_name.text = contact.name

        c_phone = ElementTree.SubElement(count, 'Phone number')
        c_phone.text = contact.phone_number

    tree = ElementTree.ElementTree(root)
    tree.write('contacts.xml')


def import_xml() -> None:
    """
    export contacts to xml file
    :return: None
        contacts.xml
    """
    data = _open_file()
    _write_file_xml(data)