"""
Задача 2. Напишите метод, который заполняет массив случайным количеством (от 1 до 100) нулей и единиц.
Размер массива должен совпадать с квадратом количества единиц в нём.

"""
import numpy as np
from random import randint as rdi

n = rdi(1,11)
print(f'count of ones = {n}')
arr = np.zeros(n**2,dtype=np.int_)

for _ in range(n):
    pos = 0
    while True:
        pos = rdi(0,len(arr)-1)
        if arr[pos] == 0:
            arr[pos] = 1
            break

print(f'size of array = {arr.size}')
print(arr)