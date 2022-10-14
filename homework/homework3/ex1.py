# Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
import numpy as np
from functools import reduce as rdc


def get_int_number(*texts): return int(input(*texts))


def create_array(low, high, length): return np.random.randint(low, high, length, dtype=np.int_)


def find_sum_odd_indexes(numbers): return rdc(lambda x, y: x + y, [numbers[i] for i in range(1, len(numbers), 2)])


def main():
    min_value = get_int_number('input min value of array: ')
    max_value = get_int_number('input max value of array: ')
    length_array = get_int_number('input length of array: ')
    numbers = create_array(min_value, max_value, length_array)
    print(numbers)
    sum_add_indexes = find_sum_odd_indexes(numbers)
    print(f'sum of values with odd indexes = {sum_add_indexes}')


if __name__ == '__main__':
    main()
