# При работе с документацией менеджер допустил
# ошибку, названия товаров перемешались с ценами. Помогите
# восстановить документ. Порядковый номер товара совпадает с
# номером цены.

line = 'туфли рубашка 2000 1000 шарф юбка шорты 1500 3000 сапоги 500 5000 брюки 1500 2000 свитер'

goods, prices = list(), list()
for word in line.split():
    if word.isdigit():
        prices.append(word)
    else:
        goods.append(word)

sells = dict(zip(goods,prices))
print(sells)