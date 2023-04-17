from typing import TypeVar
from random import randint as ri

_T = TypeVar('_T', bound='list[int]')


class ArrayLengthException(Exception):
    pass


def create_arr_int(n: int, min_val: int = 0, max_val: int = 50) -> _T:
    for i in {n, min_val, max_val}:
        if not type(i) == int:
            raise TypeError(f'{i} must be type of int')
    return [ri(min_val, max_val) for _ in range(n)]


def create_passing_arrs(mi: int = 0, ma: int = 50) -> tuple[_T, _T]:
    len_of_arr = 15
    arr1 = create_arr_int(len_of_arr, mi, ma)
    arr2 = create_arr_int(len_of_arr, mi, ma)
    return arr1, arr2


def create_raising_arrs(mi: int = 0, ma: int = 50) -> tuple[_T, _T]:
    len_of_first = 10
    len_of_second = 15
    arr1 = create_arr_int(len_of_first, mi, ma)
    arr2 = create_arr_int(len_of_second, mi, ma)
    return arr1, arr2
