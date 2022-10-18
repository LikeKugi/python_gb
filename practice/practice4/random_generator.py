# Создайте собственный генератор случайных чисел на основе числа π.

import time
from random import uniform as ru
from functools import reduce


def finding_pi():
    pi = 3
    for i in range(2, 10 ** 7):
        pi += 4 / (i * (i + 1) * (i + 2)) * (-1, 1)[i % 2 == 0]
    return (str(pi)+str(pi**2)+str(pi**3)).replace('.','')


def random_gen():
    key = finding_pi()
    pos = str(int(time.time()))
    current = (reduce(lambda x, y: x + y, map(int, pos))//2)%len(key)
    return key[current] if key[current].isdigit() else key[(current-1)%len(key)]


print(random_gen())
