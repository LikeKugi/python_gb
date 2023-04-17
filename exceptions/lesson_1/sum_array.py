# Реализуйте метод, принимающий в качестве аргумента целочисленный двумерный массив.
# Необходимо посчитать и вернуть сумму элементов этого массива.
# При этом накладываем на метод 2 ограничения: метод может работать только с квадратными массивами
# (кол-во строк = кол-ву столбцов), и в каждой ячейке может лежать только значение 0 или 1.
# Если нарушается одно из условий, метод должен бросить RuntimeException с сообщением об ошибке.
from array import array
from random import uniform
from random import randint as ri


class SquareException(Exception):
    pass


_A = array
_T = list[_A]


def sum_of_arr(arr: _T):
    total = 0
    for row in arr:
        if not type(row) == _A:
            raise TypeError(f'TypeError {row} Not type of array')
        if len(row) != len(arr):
            raise SquareException('SquareException: not a square array')
        for el in row:
            if not 0 <= el <= 1:
                raise ValueError(f'ValueError: {el} not in [0, 1]')
            total += el
    return total


def test_true():
    dimensions = 10
    matrix = [array('f', [uniform(0, 1) for _ in range(dimensions)]) for _ in range(dimensions)]
    print(*matrix, sep='\n')
    print(sum_of_arr(matrix))


def test_type_exception():
    dm = 5
    mt = [[uniform(0, 1) for _ in range(dm)] for _ in range(dm)]
    print(*mt, sep='\n')
    try:
        print(sum_of_arr(mt))
    except TypeError as e:
        print(f'TypeError: {e}')


def test_square_exception():
    mt = [array('f', [uniform(0, 1) for _ in range(ri(0, 15))]) for _ in range(ri(0, 15))]
    print(*mt, sep='\n')
    try:
        print(sum_of_arr(mt))
    except SquareException as e:
        print(f'Exception: {e}')


def test_value_exception():
    dimensions = 10
    mt = [array('f', [uniform(0, 5) for _ in range(dimensions)]) for _ in range(dimensions)]
    print(*mt, sep='\n')
    try:
        print(sum_of_arr(mt))
    except ValueError as e:
        print(f'Exception: {e}')


def main():
    test_square_exception()


if __name__ == '__main__':
    main()
