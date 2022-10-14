# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#
import numpy as np
import math


def get_int_number(*texts): return int(input(*texts))


def create_array(low, high, length): return np.random.randint(low, high, length, dtype=np.int_)


def create_range_pairs(numbers): return [numbers[i] * numbers[len(numbers) - 1 - i] for i in
                                         range(math.ceil(len(numbers) / 2))]


def main():
    min_value = get_int_number('input min value of array: ')
    max_value = get_int_number('input max value of array: ')
    length_array = get_int_number('input length of array: ')
    numbers = create_array(min_value, max_value, length_array)
    print(f'array:\n{numbers}')
    pairs = create_range_pairs(numbers)
    print(f'array of pairs:\n{pairs}')


if __name__ == '__main__':
    main()
