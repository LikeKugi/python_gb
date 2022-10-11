# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

from math import factorial as fc


def create_range_factorials(n): return [fc(i) for i in range(1, n + 1)]


def ask_number(): return int(input('enter value N: '))


def main():
    n = ask_number()
    numbers = create_range_factorials(n)
    print(*numbers)
