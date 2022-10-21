# Задайте список из 15 случайных чисел.
# Выведите все пары кратных чисел из этого списка.
from random import randrange as rr


def get_int_number(*args): return int(input(*args))


def create_range(n=15, min_value=1, max_value=100): return [rr(min_value, max_value + 1) for _ in range(n)]


def filter_elements(numbers):
    dividers = set()
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            if numbers[i]%numbers[j]==0 and (min(numbers[i],numbers[j]),max(numbers[i],numbers[j])) not in dividers:
                print((min(numbers[i],numbers[j]),max(numbers[i],numbers[j])))
                dividers.add((min(numbers[i],numbers[j]),max(numbers[i],numbers[j])))


def main():
    numbers = create_range()
    print('list of random values:\n', *numbers)
    print('list of dividers:\n',)
    filter_elements(numbers)


if __name__ == '__main__':
    main()
