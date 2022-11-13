import model as md


def _get_choose(): return input().lower()


def _action(query):
    match query:
        case '1':
            md.create()
        case '2':
            md.search()
        case '3':
            md.print_contacts()
        case '4':
            md.import_xml()
        case '5':
            md.import_html()
        case _:
            return


def main():
    for query in iter(_get_choose, 'q'):
        _action(query)
        print('1 to add contact: ')
        print('2 to search contact: ')
        print('3 to print all contacts: ')
        print('4 import contacts to xml: ')
        print('5 import contacts to html: ')
        print('q quit: ')

