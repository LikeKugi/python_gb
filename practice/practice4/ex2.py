# Актёров разделили на списки по трём качествам
# «умные», «красивые», «сильные». На главную роль нужен актёр
# обладающий всеми тремя качествами. Определите, сколько есть
# претендентов на главную роль. Списки актёров поместите в
# соответствующие файлы.

with open('handsome.txt', 'r', encoding='utf-8') as inf:
    handsome = set(map(str.rstrip, inf.readlines()))


with open('smart.txt', 'r', encoding='utf-8') as inf:
    smart = set(map(str.rstrip, inf.readlines()))

with open('strong.txt', 'r', encoding='utf-8') as inf:
    strong = set(map(str.rstrip, inf.readlines()))


print(*(handsome&smart&strong),sep='\n')