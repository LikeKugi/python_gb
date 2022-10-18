# Создайте кортеж, заполненный случайными
# числами. Напишите метод, который заменяет элемент
# в кортеже по заданному индексу.

from random import randrange as rr


def get_int_number(*args): return int(input(*args))


def create_tuple(length):
    return tuple(rr(10) for _ in range(length))


def change_el_tuple(tup):
    element = get_int_number('value to add: ')
    position = get_int_number('position: ')
    out = list(tup)
    out[position - 1] = element
    return tuple(out)


def main():
    n = get_int_number('input length of tuple: ')
    numbers = create_tuple(n)
    print(numbers)
    new_numbers = change_el_tuple(numbers)
    print(new_numbers)


if __name__ == '__main__':
    main()
