"""
Напишите программу, которая на вход принимает два
числа и проверяет, является ли одно число квадратом
другого.

"""

a,b = int(input('input number: ')),int(input('input number: '))
if a ** 2 == b or b ** 2 == a:
    print('yes')
else:
    print('no')