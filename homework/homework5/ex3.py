# Задайте список случайных чисел от 1 до 10.
# Посчитайте, сколько всего совпадающих элементов есть в списке. Удалите все повторяющиеся элементы.
from random import randrange as rr


def get_int_number(*args): return int(input(*args))


def create_range(n, min_value=1, max_value=10): return [rr(min_value, max_value + 1) for _ in range(n)]


def filter_elements(numbers:list): return list(filter(lambda x: numbers.count(x) == 1, numbers))



def main():
    length = get_int_number('enter length of a list: ')
    numbers = create_range(length)
    print('list of random values:\n', *numbers)
    non_repeat_numbers = filter_elements(numbers)
    print('list with unique values:\n', *non_repeat_numbers)
    print(f'count of repeated elements: {(len(numbers)-len(non_repeat_numbers))*2}')

if __name__ == '__main__':
    main()