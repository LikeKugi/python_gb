"""
Дано трёхзначное число N. Определить кратна ли трём сумма всех его цифр.
"""
digits = [int(digit) for digit in input()]
if sum(digits)%3 == 0:
    print('YES')
else:
    print('NO')