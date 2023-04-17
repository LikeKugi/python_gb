# Реализуйте метод checkArray(Integer[] arr), принимающий в качестве аргумента целочисленный одномерный массив.
# Метод должен пройтись по каждому элементу и проверить что он не равен null.
# А теперь реализуйте следующую логику:
# Если в какой-то ячейке встретился null, то необходимо “оповестить” об этом пользователя
# Если null’ы встретились в нескольких ячейках, то идеально было бы все их “подсветить
from random import randint as ri


def check_arr(arr: list[int | None]) -> list[int] | bool:
    out_exceptions = []
    for i, el in enumerate(arr):
        if el is None:
            out_exceptions.append(i)
    if out_exceptions:
        raise ValueError(f'ValueError: {out_exceptions} are None')
    return True


def create_array_nones():
    arr = [ri(0, 50) if ri(0, 4) > 2 else None for _ in range(ri(5, 10))]
    return arr


def create_array():
    arr = [ri(0, 50) for _ in range(ri(5, 10))]
    return arr


def main():
    arr_nones = create_array_nones()
    print(arr_nones)
    try:
        print(check_arr(arr_nones))
    except ValueError as e:
        print(e)

    arr = create_array()
    print(arr)
    print(check_arr(arr))


if __name__ == '__main__':
    main()
