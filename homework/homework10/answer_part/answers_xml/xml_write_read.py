import os
from xml.etree import ElementTree

FILE = 'questions.xml'


def create_new_file() -> None:
    root = ElementTree.Element('questions')

    paragraphs = ElementTree.SubElement(root, 'questions')
    paragraphs.text = 'Questions from users'

    tree = ElementTree.ElementTree(root)
    write_file(tree)


def write_file(tree: ElementTree) -> None:
    tree.write(FILE, encoding='utf-8', xml_declaration=True)


def read_file() -> ElementTree:
    if not os.path.exists(FILE) or os.stat(FILE).st_size == 0:
        create_new_file()

    tree = ElementTree.parse(FILE)

    root = tree.getroot()
    return root
