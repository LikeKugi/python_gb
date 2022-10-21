# Задайте список случайных чисел от 1 до 10, выведите все элементы больше 5. Используйте для решения лямбда-функцию.
from random import randrange as rr


def get_int_number(*args): return int(input(*args))


def create_range(n, min_value=1, max_value=10): return [rr(min_value, max_value + 1) for _ in range(n)]


def filter_elements(numbers): return filter(lambda x: x > 5, numbers)


def main():
    length = get_int_number('enter length of a list: ')
    numbers = create_range(length)
    print('list of random values:\n', *numbers)
    print('filtred list with values > 5:\n', *filter_elements(numbers))


if __name__ == '__main__':
    main()
