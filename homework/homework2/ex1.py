# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

from functools import reduce


def get_digits_number(): return [int(digit) for digit in input() if digit.isdigit()]


def find_sum_digits(digits): return reduce(lambda x, y: x + y, digits)


def main():
    number = get_digits_number()
    sum_of_digits = find_sum_digits(number)
    print(sum_of_digits)


if __name__ == '__main__':
    main()
