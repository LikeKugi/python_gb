# Строки, состоящие из последовательностей цифр,
# формируются следующим образом. Первая строка состоит из
# четырех единиц. Каждая из последующих строк создается
# следующим действием: берется предыдущая строка и после
# каждой ее цифры вставляется цифра на единицу большая. Вот
# первые 3 строки, созданные по этому правилу:
# (1) 1111
# (2) 12121212
# (3) 1223122312231223
# Сколько цифр 5 и сколько цифр 7 будет в строке с номером
# (9)?
# В ответе укажите через пробел два целых числа: сначала
# количество цифр 5 в девятой строке, а затем количество цифр
# 7 в девятой строке.
from collections import deque
from collections import Counter


def count():
    line = '1111'
    numbers = deque(map(int, [a for a in line]))
    new_numbers = deque([])

    for i in range(8):
        while numbers:
            a = numbers.popleft()
            new_numbers.extend([a, a + 1])
        numbers, new_numbers = new_numbers, numbers
        print(numbers)
        print(i + 2, Counter(numbers))


if __name__ == '__main__':
    count()
