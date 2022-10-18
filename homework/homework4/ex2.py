# В первой строке файла находится информация об ассортименте мороженного,
# во второй - информация о том, какое мороженное есть на складе.
# Выведите названия того товара, который закончился.

with open('icecream.txt', 'r', encoding='utf-8') as inf:
    assortment = set(inf.readline().rstrip().split(', '))
    current = set(inf.readline().rstrip().split(', '))
    print(f'Закончилось:', *assortment - current)
