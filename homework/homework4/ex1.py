# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
import math


def get_int_number(): return int(input())


def check_prime(n: int, divigers: list):
    if n % 2 == 0:
        divigers.append(2)
        return n // 2
    if n % 3 == 0:
        divigers.append(3)
        return n // 3
    for i in range(1, math.ceil(n ** 0.5) + 1):
        if n % (6 * i - 1) == 0:
            divigers.append(6 * i - 1)
            return n // (6 * 1 - 1)
        if n % (6 * i + 1) == 0:
            divigers.append(6 * i + 1)
            return n // (6 * i + 1)


def find_divigers(number: int):
    divigers = []
    while number != 1:
        number = check_prime(number, divigers)
    return divigers


def main():
    n = get_int_number()
    divigers = find_divigers(n)
    print(f'prime divigers of {n}:\n',*divigers)


if __name__ == '__main__':
    main()
