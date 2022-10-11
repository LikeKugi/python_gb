# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.
import numpy as np
from random import randint as ri
import os


def get_number(): return abs(int(input()))


def create_range(n: int): return np.random.randint(-n, n + 1, size=n)


def check_file(): return os.path.exists('file.txt')


def create_file(n):
    positions = ri(2, n)
    used_positions = set()
    with open('file.txt', 'w') as ouf:
        for i in range(positions + 1):
            current = ri(1, n)
            if current in used_positions:
                continue
            used_positions.add(current)
            ouf.write(str(current) + '\n')


def read_from_file():
    positions = list()
    with open('file.txt') as inf:
        for line in inf:
            positions.append(int(line))
    return positions


def product_positions(numbers: np.array, pos: list):
    product = 1
    for index in pos:
        product *= numbers[index]
    return product


def main():
    n = get_number()
    numbers = create_range(n)
    if not check_file():
        create_file(n)
    positions = read_from_file()
    product = product_positions(numbers,positions)
    print(product)

main()
