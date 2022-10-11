"""
Дан отсортированный массив, заполненный случайными вещественными числами.
Найдите ближайший к среднему арифметическому максимума и минимума элемент массива.
"""
import numpy as np


def get_length(): return int(input())


def create_range(): return np.arange(-5, 10, 0.2)


def find_closest(numbers: np.array):
    max_value = max(numbers)
    min_value = min(numbers)
    average = max_value + min_value / 2
    return find_nearest(numbers, value=average)


def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return array[idx]


def main():
    numbers = create_range()
    print(numbers)
    print(find_closest(numbers))


if __name__ == '__main__':
    main()
