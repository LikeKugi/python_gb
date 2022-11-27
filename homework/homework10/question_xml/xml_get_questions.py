from .xml_write_read import read_file


def _get_tree():
    root = read_file()
    return root


def looking_for_questions(user_id: int, *, need_answer=False) -> dict:
    root = _get_tree()
    asked_questions = {}
    for question in root.findall('article'):
        user = int(question.find('fromUser').text)
        time_question = question.find('time').text
        ask = question.find('question').text
        answer = question.find('answer').text
        if user == user_id:
            if (not need_answer) or (need_answer and answer):
                asked_questions[time_question] = [ask, answer]
    return asked_questions


def looking_for_unanswered_questions(user_id: int | None) -> dict:
    root = _get_tree()
    asked_questions = {}
    for question in root.findall('article'):
        user = int(question.find('fromUser').text)
        time_question = question.find('time').text
        ask = question.find('question').text
        answer = question.find('answer').text
        if not answer and ((not user) or (user_id == user)):
            asked_questions[time_question] = [ask, answer]
    return asked_questions
