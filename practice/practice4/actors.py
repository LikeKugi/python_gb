handsome = set()
smart = set()
strong = set()

with open('handsome.txt', encoding='utf-8') as inf:
    for line in inf.readlines():
        handsome.add(line.rstrip())

print(handsome)

with open('smart.txt', encoding='utf-8') as inf:
    for line in inf.readlines():
        smart.add(line.rstrip())

print(smart)

with open('strong.txt', encoding='utf-8') as inf:
    for line in inf.readlines():
        strong.add(line.rstrip())

print(strong)

for el in handsome & smart & strong:
    print(el)
