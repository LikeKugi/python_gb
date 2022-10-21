# Дан список случайных чисел. Создайте список, в который попадают числа, описывающие возрастающую последовательность.
# Порядок элементов менять нельзя.
from random import randrange as rr


def get_int_number(*args): return int(input(*args))


def create_range(n, min_value=1, max_value=20): return [rr(min_value, max_value + 1) for _ in range(n)]


def filter_elements(numbers):
    result = [numbers[0]]
    for el in numbers:
        if el > result[-1]:
            result.append(el)
    return result


def main():
    length = get_int_number('enter length of a list: ')
    numbers = create_range(length)
    print('list of random values:\n', *numbers)
    print('filtred list with rising values:\n', *filter_elements(numbers))


if __name__ == '__main__':
    main()
