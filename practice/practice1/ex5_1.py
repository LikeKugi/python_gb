numbers = [int(el) for el in input().split()]
max_el = min_el = numbers[0]
for number in numbers:
    if number > max_el:
        max_el = number
    elif number < min_el:
        min_el = number
print(*numbers)
print(f'max = {max_el}')
print(f'min = {min_el}')