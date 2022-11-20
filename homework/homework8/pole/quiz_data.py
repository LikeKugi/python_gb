import pickle


def create_word_dict(word: str) -> dict[str, list[int]]:
    """
    make dict from word
    key is letter, value is list of indexes the letter in the word
    :param word: str
        any word
    :return: dict[str, list[int]]
        str - every char
        list[int] - indexes
    """
    answer_dict = {}
    for i, char in enumerate(word):
        answer_dict.setdefault(char, [])
        answer_dict[char].append(i)
    return answer_dict


def create_db() -> None:
    """
    creating pickle file with dict quizes
    :return: None
        quiz.bin
    """
    quiz_dict = {}
    with open('quiz.txt', 'r', encoding='utf-8') as inf:
        questions = inf.readlines()
        for i, line in enumerate(questions):
            answer, question = line.rstrip().split('; ')

            answer_dict = create_word_dict(answer.upper())

            quiz_dict[i] = {
                'query': question,
                'answer': answer_dict
            }

    with open('quiz.bin','wb') as ouf:
        pickle.dump(quiz_dict, ouf)

