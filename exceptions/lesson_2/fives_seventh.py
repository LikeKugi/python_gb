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
from functools import lru_cache


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


# Algorithmic count

# 1	1:4
# 2	1:4 2:4
# 3	1:4 2:8 3:4
# 4	1:4 2:12 3:12 4:4
# 5	1:4 2:16 3:24 4:16 5:4
# 6	1:4 2:20 3:40 4:40 5:20 6:4
# 7	1:4 2:24 3:60 4:80 5:60 6:24 7:4
# 8	1:4 2:28 3:84 4:140 5:140 6:84 7:28 8:4
# 9	1:4 2:32 3:112 4:224 5:280 6:224 7:112 8:32 9:4
# ...

def algorithmic_count():
    count_five = recursive_counter(5, 9)
    print(f'5: {count_five}')

    count_seven = recursive_counter(7, 9)
    print(f'7: {count_seven}')


@lru_cache()
def recursive_counter(n, line):
    if n == 1 or n == line:
        return 4
    return recursive_counter(n, line - 1) + recursive_counter(n - 1, line - 1)


if __name__ == '__main__':
    algorithmic_count()
