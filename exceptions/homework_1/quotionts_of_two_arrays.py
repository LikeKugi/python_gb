# Реализуйте метод, принимающий в качестве аргументов два целочисленных массива, и возвращающий новый массив,
# каждый элемент которого равен частному элементов двух входящих массивов в той же ячейке.
# Если длины массивов не равны, необходимо как-то оповестить пользователя.
# Важно: При выполнении метода единственное исключение, которое пользователь может увидеть - RuntimeException,
# т.е. ваше.

from typing import TypeVar

from create_arrays import ArrayLengthException, create_raising_arrs, create_passing_arrs

_T = TypeVar('_T', bound='list[int]')


def divide_arrays(arr1: _T, arr2: _T) -> _T:
    if len(arr1) != len(arr2):
        raise ArrayLengthException(f'ArrayLengthException: {len(arr1)} != {len(arr2)}')
    out = []
    for i, (el1, el2) in enumerate(zip(arr1, arr2)):
        if arr2[i] == 0:
            raise ArithmeticError(f'Divide by Zero: {el2} == 0')
        out.append(el1 / el2)
    return out


def passing_tests() -> _T:
    arr1, arr2 = create_passing_arrs(1, 50)
    print(f'a1: {" ".join(map(str, arr1))}')
    print(f'a2: {" ".join(map(str, arr2))}')
    out = divide_arrays(arr1, arr2)
    return out


def raising_tests() -> _T:
    arr1, arr2 = create_raising_arrs(1, 50)
    print(f'a1: {" ".join(map(str, arr1))}')
    print(f'a2: {" ".join(map(str, arr2))}')
    out = divide_arrays(arr1, arr2)
    return out


def main():
    for name in [passing_tests, raising_tests]:
        try:
            out = name()
            print(out)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
