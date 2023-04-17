# Реализуйте метод, принимающий в качестве аргументов два целочисленных массива, и возвращающий новый массив,
# каждый элемент которого равен разности элементов двух входящих массивов в той же ячейке.
# Если длины массивов не равны, необходимо как-то оповестить пользователя.

from typing import TypeVar

from create_arrays import ArrayLengthException, create_raising_arrs, create_passing_arrs

_T = TypeVar('_T', bound='list[int]')


def diff_arrays(arr1: _T, arr2: _T) -> _T:
    if len(arr1) != len(arr2):
        raise ArrayLengthException(f'ArrayLengthException: {len(arr1)} != {len(arr2)}')
    return [a - b for a, b in zip(arr1, arr2)]


def main():
    for a1, a2 in [create_passing_arrs(), create_raising_arrs()]:
        print(f'a1: {" ".join(map(str, a1))}')
        print(f'a2: {" ".join(map(str, a2))}')
        try:
            a3 = diff_arrays(a1, a2)
            print(f'a3: {" ".join(map(str, a3))}')
        except ArrayLengthException as e:
            print(e)


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
