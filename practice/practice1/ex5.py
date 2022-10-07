"""
Напишите программу, которая находит наибольшее и
наименьшее число из списка значений
"""

numbers = [int(el) for el in input().split()]
print(f'max = {max(numbers)}')
print(f'min = {min(numbers)}')
