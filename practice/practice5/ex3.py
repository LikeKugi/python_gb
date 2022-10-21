# Имеется информация о том, телефонами
# каких компаний сейчас торгуют магазины.
# Определите те компании, чьи телефоны
# присутствуют в каждом магазине.
from functools import reduce

with open('Телефоны.txt', encoding='utf-8') as inf:
    stores = {}
    for line in inf.readlines():
        if line[0].isdigit():
            key = line.rstrip()
        else:
            stores[key] = set(line.lower().rstrip().split(', '))
print(stores)
result = reduce(lambda x, y: x & y, stores.values())
print(result)

