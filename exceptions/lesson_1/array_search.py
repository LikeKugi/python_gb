# Реализуйте метод, принимающий в качестве аргумента целочисленный массив и некоторое значение.
# Метод ищет в массиве заданное значение и возвращает его индекс. При этом, например:
# если длина массива меньше некоторого заданного минимума, метод возвращает -1, в качестве кода ошибки.
# если искомый элемент не найден, метод вернет -2 в качестве кода ошибки.
# если вместо массива пришел null, метод вернет -3
# придумайте свои варианты исключительных ситуаций и верните соответствующие коды ошибок.
# Напишите метод, в котором реализуйте взаимодействие с пользователем.
# То есть, этот метод запросит искомое число у пользователя, вызовет первый, обработает возвращенное
# значение и покажет читаемый результат пользователю. Например, если вернулся -2,
# пользователю выведется сообщение: “Искомый элемент не найден”.
from random import randint as ri
from random import uniform as un

_T = list[int]


def find_in_arr(arr: _T, query: int, ml: int) -> int:
    if not type(arr) == list:
        return -3
    if len(arr) < ml:
        return -1
    for i, el in enumerate(arr):
        if not (type(el)) == int:
            return -2
        if el == query:
            print(el, query)
            return i
    else:
        return -1


def main():
    query = 5
    min_len = 25
    arr1 = [i for i in range(20)]
    print(arr1)
    print(find_in_arr(arr1, query, min_len))
    arr2 = [ri(-30, 100) for _ in range(15)]
    print(arr2)
    print(find_in_arr(arr2, query, min_len))
    arr3 = [un(-30, 30) for _ in range(30)]
    print(arr3)
    print(find_in_arr(arr3, query, min_len))
    print(find_in_arr(None, query, min_len))


if __name__ == '__main__':
    main()
