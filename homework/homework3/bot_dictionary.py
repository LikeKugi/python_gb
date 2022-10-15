# Создайте скрипт бота, который находит ответы на фразы по ключу в словаре.
# Бот должен, как минимум, отвечать на фразы «привет», «как тебя зовут».
# Если фраза ему неизвестна, он выводит соответствующую фразу.

from random import randrange as RR


def get_phrase(*texts): return input(*texts)


def analyse_phrase(phrases, phrase):
    if phrase.lower() in {'q', 'й', 'stop', 'все', 'всё', 'стоп'}:
        print('CHAO!!!')
        return False
    if phrase.lower() in phrases:
        print(phrases.get(phrase)[RR(len(phrases.get(phrase)))])
    else:
        phrases[phrase.lower()] = new_phrase()
    return True


def returning(): return


def greeting():
    answers = {
        0: 'Моё почтение.',
        1: 'Привет!',
        2: 'Здравствуй!',
        3: 'Приветик!',
        4: 'Салют!',
        5: 'Приветствую вас!'
    }
    print(answers.get(RR(len(answers))))


def new_phrase():
    new_variant = {}
    print('Я не понимаю, скажи 3 варианта ответа на эту фразу: ')
    for i in range(3):
        answer = get_phrase(f'{i + 1} вариант: ')
        new_variant[i] = answer
    return new_variant


def main():
    greeting()
    phrases = {
        'привет': {
            0: 'Моё почтение.',
            1: 'Привет!',
            2: 'Здравствуй!',
            3: 'Приветик!',
            4: 'Салют!',
            5: 'Приветствую вас!'
        },
        'как тебя зовут': {
            0: 'Ботик',
            1: 'Я Бот, вырасту и захвачу мир',
            2: 'Меня зовут... Босс',
            3: 'Я Бот, кек'
        },
    }
    chatting = True
    while chatting:
        chatting = analyse_phrase(phrases, get_phrase())


main()
