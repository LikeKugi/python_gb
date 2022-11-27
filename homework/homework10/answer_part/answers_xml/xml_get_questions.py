from .xml_write_read import read_file


def _get_tree():
    root = read_file()
    return root


def looking_for_unanswered_questions(user_id: int | None = None) -> dict:
    root = _get_tree()
    query_questions = {}
    for i, question in enumerate(root.findall('article')):
        user = int(question.find('fromUser').text)
        question_id = int(question.find('messageID').text)
        ask = question.find('question').text
        answer = question.find('answer').text



        if not answer and ((not user_id) or (user_id == user)):
            query_questions[i] = {
                'user_id': user,
                'message_id': question_id,
                'question_text': ask,
                'answer_text': answer
            }

    print(query_questions)
    return query_questions
