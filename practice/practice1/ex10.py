"""
Задача 1. Задан массив из случайных цифр на 15 элементов.
На вход подаётся трёхзначное натуральное число.
Напишите программу, которая определяет, есть в массиве последовательность из трёх элементов,
совпадающая с введённым числом.

{0, 5, 6, 2, 7, 7, 8, 1, 1, 9} - 277 -> да
{4, 4, 3, 6, 7, 0, 8, 5, 1, 2} - 812 -> нет

"""
import numpy as np

digits = np.random.randint(0, 10, size=15)
print(digits)
number_find = [int(digit) for digit in input()]
for i in range(digits.shape[0]):
    if digits[i] == number_find[0]:
        for j in range(1, len(number_find)):
            if digits[i + j] != number_find[j]:
                break
        else:
            print('YES')
            break
else:
    print('NO')
