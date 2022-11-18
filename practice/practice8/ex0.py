# Задайте двумерный массив случайных
# чисел размером 4х5. Случайные числа не должны
# повторяться. Запишите массив в txt-файл.
from random import randint as RI


def fill_random_2d_array(array):
    used_numbers = set()

    for i in range(4):
        j = 0
        while 0 in array[i]:
            el = RI(1, 1000)
            if el not in used_numbers:
                array[i][j] = el
                j += 1


def create_file(array):
    with open('array.txt', 'w') as ouf:
        for row in array:
            print(*row, file=ouf)

def read_from_file():
    with open('array.txt') as inf:
        data = []
        for line in inf.readlines():
            data.append(list(map(int, line.rstrip().split())))
    return data


def main():
    # array = [[0] * 5 for _ in range(4)]
    # fill_random_2d_array(array)
    # create_file(array)

    new_array =  read_from_file()
    flat_arr = sorted([el for row in new_array for el in row])

    print(flat_arr[-2] - flat_arr[0])


if __name__ == '__main__':
    main()