#  Используя рекурсию, выведите остаток от деления числа a на число b.

a = int(input())
b = int(input())


def find_reminder(a: int, b: int):
    if a < b:
        return a
    else:
        return find_reminder(a - b, b)


print(find_reminder(a, b))
