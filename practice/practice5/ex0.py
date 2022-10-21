# С помощью анонимной функции найдите в
# списке на 15 элементов числа, кратные 5. Заполните
# список случайным образом числами от 1 до 100.

from random import randrange as rr


def get_int_number(*args): return int(input(*args))


def create_range(n=15, min_value=1, max_value=100): return [rr(min_value, max_value + 1) for _ in range(n)]


def filter_elements(numbers): return filter(lambda x: x % 5 == 0, numbers)


def main():
    numbers = create_range()
    print('list of random values:\n', *numbers)
    print('filtred list with values % 5 == 0:\n', *filter_elements(numbers))


if __name__ == '__main__':
    main()
