# Дано число N. Найдите площадь круга с
# радиусом N. Ответ округлите до сотых.
from math import pi as PI

r = int(input())
print(round(PI * r ** 2, 2))
