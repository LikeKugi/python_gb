AVAILABLE_CHARS = set(chr(i) for i in range(ord('А'), ord('Я')))


def ask(used_chars: set) -> str:
    """
    ask player for a letter
    :param used_chars: set
        letters that were used in current game
    :return: str
        letter that wasn't used or quit command
    """
    print('/-------------------------------------------------/')
    print('Доступные буквы: ')
    print(*sorted(AVAILABLE_CHARS - used_chars))
    print('/-------------------------------------------------/')

    while True:
        print('"Q", "СТОП", "-" чтобы прекратить игру')
        char = input('Введите букву: ').upper()

        if char in {'Q', 'СТОП', '-'}:
            return char

        if char in used_chars:
            print('Эта буква уже была')
            continue

        if char not in AVAILABLE_CHARS:
            print('Введите букву русского алфавита кроме ё')
            continue

        used_chars.add(char)
        return char
