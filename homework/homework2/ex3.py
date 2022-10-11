# Даны две строки. Посчитайте сколько раз каждый символ первой строки встречается во второй
# «one» «onetwonine» - o – 2, n – 3, e – 2

line1 = input()
line2 = input()

for el in set(line1):
    print(el,': ',line2.count(el))