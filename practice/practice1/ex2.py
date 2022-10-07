"""
Организуйте последовательный ввод чисел до тех
пор, пока не будет введён 0. Подсчитайте среди
введённых чисел те, которые кратны трём.

"""
number = None
counter = 0
while number!=0:
    number = int(input())
    if number % 3 == 0:
        counter += 1
print(counter)
