# Даны три числовых массива.
# Реализуйте метод, в который определяет в каком из первых двух массивов чаще всего встречаются элементы третьего.
import numpy as np

numbers1 = list(np.random.randint(0, 20, size=15))
print(numbers1)
numbers2 = list(np.random.randint(0, 20, size=15))
print(numbers2)
numbers3 = list(np.random.randint(0, 20, size=15))
print(numbers3)
counter_1 = {}
counter_2 = {}
for number in set(numbers3):
    counter_1[number] = numbers1.count(number)
    counter_2[number] = numbers2.count(number)

if sum(counter_1.values()) != sum(counter_2.values()):
    print(('1', '2')[sum(counter_1.values()) < sum(counter_2.values())])
else:
    print('pair')
