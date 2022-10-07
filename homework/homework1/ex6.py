"""
Напишите программу, которая на вход
принимает число (N), а на выходе показывает все чётные
числа от 1 до N.
"""


def get_int_number(): return int(input('input number > 2: '))


def find_range(n: int):
    """
     find even numbers in range n
     :param n: int
     :return: list
     >>> find_range(5)
     [2, 4]
     >>> find_range(8)
     [2, 4, 6, 8]
     """
    assert n > 2, 'n should be > 2, your n is: '+ n
    return [el for el in range(2, n + 1, 2)]


def main():
    n = get_int_number()
    numbers = find_range(n)
    print(*numbers)


if __name__ == '__main__':
    main()
