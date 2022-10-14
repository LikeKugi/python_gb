# Дан файл, заполненный числами построчно.
# Считайте файл. Выведите все элементы, стоящие на
# чётных строках, а потом на нечётных.
from random import randint as ri
import os


def get_number(): return abs(int(input()))


def check_file(): return os.path.exists('numbers.txt')


def create_file(n):
    positions = ri(n, 5 * n)
    used_positions = set()
    with open('numbers.txt', 'w') as ouf:
        for i in range(positions + 1):
            current = ri(1, n)
            if current in used_positions:
                continue
            used_positions.add(current)
            ouf.write(str(current) + '\n')


def read_from_file():
    positions = list()
    with open('numbers.txt') as inf:
        positions.extend([int(line.replace('\n', '')) for line in inf])
    return positions


def main():
    n = get_number()
    if not check_file() or n % 2:
        create_file(n)
    positions = read_from_file()
    print(positions[::2] + positions[1::2])


if __name__ == '__main__':
    main()
