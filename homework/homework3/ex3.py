# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
import numpy as np


def get_int_number(*texts): return int(input(*texts))


def create_array(low, high, length): return np.random.uniform(low, high, length)


def find_diff_tails(numbers):
    tails = list(map(lambda x: x % 1, numbers))
    return max(tails) - min(tails)


def main():
    min_value = get_int_number('input min value of array: ')
    max_value = get_int_number('input max value of array: ')
    length_array = get_int_number('input length of array: ')
    numbers = create_array(min_value, max_value, length_array)
    print(f'array:\n{numbers}')
    diff_fractional = find_diff_tails(numbers)
    print(f'difference between max and min fractional parts:\n{diff_fractional}')


if __name__ == '__main__':
    main()
