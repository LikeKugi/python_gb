# На вход подаётся четырёхзначное число.
# Получите список, состоящий из цифр данного числа,
# увеличенных на 10.

number = list(map(lambda x: int(x)+10, input()))
print(number)