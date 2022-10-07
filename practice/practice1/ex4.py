"""
Напишите программу, которая будет принимать на вход дробь
и показывать первую цифру дробной части числа.

"""


def find_digit():
    n = float(input())
    fl_part = int(n) - n
    print(abs(int(fl_part * 10)) if int(n) != n else 'NO')


def find_from_string():
    number = input()
    print(number[number.find('.') + 1] if number.find('.') > 0 else -1)


def find_3_digits():
    number = float(input())
    number %= 1
    print(int(number*10))
    print(number)

find_3_digits()