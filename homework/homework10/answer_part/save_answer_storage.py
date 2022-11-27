from .answer_storage import Answer
from .answers_xml import write_answer


def _find_article(questions: dict, primary_key: int):
    current_answer = Answer()

    current_answer.user_id = questions.get(primary_key).get('user_id')
    current_answer.message_id = questions.get(primary_key).get('message_id')
    current_answer.question_text = questions.get(primary_key).get('question_text')

    return current_answer


def save_answer(questions: dict, i: int, answer: str):
    current_answer = _find_article(questions, i)
    current_answer.answer_text = answer
    print(current_answer)
    write_answer(current_answer.user_id, current_answer.message_id, current_answer.answer_text)
    return current_answer
