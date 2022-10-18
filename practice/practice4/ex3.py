#  Сгенерируйте список случайных чисел от
# 1 до 20, состоящий из 10 элементов. Удалите из
# списка дубликаты уже имеющихся элементов
from random import randrange as rr
numbers = [rr(1,21) for _ in range(10)]
print(numbers)
print(list(set(numbers)))