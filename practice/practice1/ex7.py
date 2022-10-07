"""
Задача 3. Дано трёхзначное число N. Определить, есть ли среди его цифр 4 или 7.

"""

digits = [int(digit) for digit in input()]
if 4 in digits or 7 in digits:
    print('YES')
else:
    print('NO')