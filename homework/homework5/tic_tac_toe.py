"""
Создайте игру в крестики-нолики.
"""
import os


def get_move(*args): return int(input(*args))


def create_field(numbers):
    print('-' * 11)
    for i in range(len(numbers)):
        for j in range(len(numbers[i])):
            print(numbers[i][j], end=' | ')
        print()
        print('-' * 11)


create_field([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
