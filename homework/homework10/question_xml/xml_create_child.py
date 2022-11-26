from xml.etree import ElementTree
from .xml_write_read import read_file, write_file
import datetime, time


def _get_date_from_message(message_time: int) -> datetime:
    formatted_time = datetime.datetime.utcfromtimestamp(message_time)
    formatted_time = formatted_time.strftime('%d-%m-%Y %H:%M:%S')
    return formatted_time


def _create_question_node(message) -> ElementTree:
    time_message = str(_get_date_from_message(message.date))
    message_id = str(message.message_id)
    user = str(message.from_user.id)
    question = message.text

    root = ElementTree.Element('question')

    xml_from_user = ElementTree.SubElement(root, 'fromUser')
    xml_from_user.text = user

    xml_message_id = ElementTree.SubElement(root, 'messageID')
    xml_message_id.text = message_id

    xml_time_message = ElementTree.SubElement(root, 'time')
    xml_time_message.text = time_message

    xml_question = ElementTree.SubElement(root, 'question')
    xml_question.text = question

    xml_answer = ElementTree.SubElement(root, 'answer')
    xml_answer.text = ''

    return root


def add_question_node(message) -> None:
    node = _create_question_node(message)
    root = read_file()
    root.append(node)
    tree = ElementTree.ElementTree(root)
    write_file(tree)