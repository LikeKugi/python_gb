import pickle
from random import randrange as RR
from os.path import exists
from quiz_data import create_db


def get_quiz_dict() -> dict[int, dict]:

    if not exists('quiz.bin'):
        create_db()

    with open('quiz.bin', 'rb') as inf:
        quiz_questions = pickle.load(inf)

    return quiz_questions


def choose_quiz(used: set, quiz: dict[int, dict]):
    ask = None
    flag = False
    while not flag:
        ask = RR(len(quiz))
        if ask not in used:
            flag = True
    used.add(ask)
    return quiz.get(ask)


