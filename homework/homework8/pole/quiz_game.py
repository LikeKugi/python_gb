from choose_word import get_quiz_dict, choose_quiz
from field import create_array_answer, put_char_in_field
from ask_user import ask


def ask_for_continue(): return input('Continue(any) or Exit(q): ')


def main_loop() -> None:
    """
    main loop of the game
    :return: None
    """
    used_words = set()
    used_chars = set()
    all_questions = get_quiz_dict()
    quiz_task = choose_quiz(used_words, all_questions)
    answer = quiz_task['answer']
    word = create_array_answer(answer)
    answer_letters = set(answer)
    while '_' in word:
        print(quiz_task['query'])
        print(*word)
        char = ask(used_chars)
        if char in {'Q', 'СТОП', '-'}:
            break
        if char in answer_letters:
            put_char_in_field(char, word, answer)

        if '_' not in word:
            print('ПОЗДРАВЛЯЮ!')
            print(*word)


def main():
    for _ in iter(ask_for_continue, 'q'):
        main_loop()


if __name__ == '__main__':
    main()
