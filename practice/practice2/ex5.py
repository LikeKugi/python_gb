"""
 Дан массив. С помощью цикла переписать его элементы в другой массив такого же размера следующим  образом:
 сначала должны  идти все  отрицательные  элементы, а  затем  все остальные.
 Использовать  только  один  проход  по исходному массиву.
"""
import numpy as np


def get_number(): return abs(int(input()))


def create_range(n: int): return np.random.randint(-n, n + 1, size=n)


def sort_numbers(numbers):
    sorted_numbers = list()
    numbers = list(numbers)
    i = 0
    while i < len(numbers):
        if numbers[i] < 0:
            sorted_numbers.append(numbers.pop(i))
        else:
            i += 1
    sorted_numbers.extend(numbers)
    return sorted_numbers


def main():
    n = get_number()
    numbers = create_range(n)
    print(*numbers)
    print(*sort_numbers(numbers))


if __name__ == '__main__':
    main()
