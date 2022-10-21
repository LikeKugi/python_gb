from functools import reduce
# 36 3*3*2*2
# 18 2*3*3
alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

with open('animals.txt') as inf:
    for line in inf.readlines():
        numbers = line.rstrip()
        chars = [numbers[i:i+6] for i in range(0,len(numbers),6)]
        print(chars)
        for char in chars:
            i = int(char,2)
            print(alphabet[i],end='')

        print()