import pickle

from .contact import Contact


def _open_file() -> dict[int, Contact]:
    with open('contacts.bin', 'rb') as inf:
        db_contacts = pickle.load(inf)
    return db_contacts


def _create_data(db_contacts: dict[int, Contact]) -> str:
    tags = """<html>  
    <head>
    </head>
    <body>
    <ul>
    """
    if db_contacts:
        for contact in db_contacts.values():
            tags += f"""<li> {contact.name}
            \t\t{contact.phone_number}</li>
            """
    tags += """</ul>
    </body>
    </html>
    """
    return tags


def _import_html_file(data: str) -> None:
    with open('contacts.html', 'w') as ouf:
        ouf.write(data)


def import_html() -> None:
    """
    import contacts to .html file
    :return: None
        contacts.html
    """
    db = _open_file()
    data = _create_data(db)
    _import_html_file(data)
