# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Сдвиньте все элементы списка на 2 позиции вправо.
# 3 -> [2, 3, -3, -2, -1, 0, 1]

import numpy as np


def get_range(): return int(input())


def create_range(n): return np.random.randint(-n, n + 1, n, dtype=np.int_)


def move_array(arr: np.array, n: int):
    output = list()
    for i in range(n):
        output.append(arr[(i - 2) % len(arr)])
    return output


def main():
    numbers = create_range(10)
    new_arr = move_array(numbers, len(numbers))
    print(numbers)
    print(new_arr)

if __name__ == '__main__':
    main()
