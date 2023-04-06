from random import randint as ri
from functools import wraps
import time

from bubble_sort import bubble_sort
from quick_sort import quickSort


def timer(func):
    @wraps(func)
    def inner(*args, **kwargs):
        start = time.time()
        returning = func(*args, **kwargs)
        end = time.time()
        print(f'{inner.__doc__} ended in {end - start}')
        return returning

    return inner


def create_arr(n: int) -> list[int]:
    arr = [ri(0, 200) for _ in range(n)]
    return arr


@timer
def quick(arr: list[int | float] ) -> None:
    """
    quicksort
    :param arr: list[int | float]
    :return: None
    """
    quickSort(arr, 0, len(arr) - 1)
    print(arr)


@timer
def bubble(arr: list[int | float]) -> None:
    """
    bubblesort
    :param arr: list[int | float]
    :return: None
    """
    bubble_sort(arr)
    print(arr)


if __name__ == '__main__':
    arr = create_arr(100_000)
    print(arr)

    quick([*arr])
    bubble([*arr])
