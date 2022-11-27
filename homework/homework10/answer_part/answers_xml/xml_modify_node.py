from xml.etree import ElementTree
from .xml_write_read import read_file, write_file


def _get_tree() -> ElementTree:
    root = read_file()
    return root


def write_answer(user, message, answer):
    root = _get_tree()

    for question in root.findall('article'):
        user_id = int(question.find('fromUser').text)
        question_id = int(question.find('messageID').text)

        if user_id == user and question_id == message:
            q = question.find('answer')
            q.text = answer

    tree = ElementTree.ElementTree(root)
    write_file(tree)
