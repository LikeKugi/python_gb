# Создайте файл random.txt. Запишите в него
# 10 случайных чисел

from random import randrange as rr

with open('random.txt','w') as ouf:
    for _ in range(10):
        ouf.write(str(rr(50))+'\n')
        