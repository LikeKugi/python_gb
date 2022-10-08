# Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет



def get_int_number(): return int(input())


def is_weekend(n: int):
    """
    check if number of the day is weekend
    :param n: int
    :return: bool
    >>> is_weekend(1)
    False
    >>> is_weekend(2)
    False
    >>> is_weekend(3)
    False
    >>> is_weekend(4)
    False
    >>> is_weekend(5)
    False
    >>> is_weekend(6)
    True
    >>> is_weekend(7)
    True
    """
    assert 0 < n < 8, "enter number of day should be in [1:7]. you entered: " + str(n)
    if n in (6, 7):
        return True
    else:  # n in [1:5]
        return False


def print_result(day: int):
    """
    print 'да' if the day is a weekend else print 'нет'
    :param day: int
    :return: None
    >>> print_result(1)
    нет
    >>> print_result(2)
    нет
    >>> print_result(3)
    нет
    >>> print_result(4)
    нет
    >>> print_result(5)
    нет
    >>> print_result(6)
    да
    >>> print_result(7)
    да
    """
    if is_weekend(day):
        print('да')
    else:
        print('нет')


def main():
    import doctest
    #doctest.testmod()

    day = -1
    while day < 1 or day > 7:
        print('Enter a number of a day:')
        try:
            day = get_int_number()
        except Exception:
            print('Plz enter number between 1 and 7')

    print_result(day)


if __name__ == '__main__':
    main()