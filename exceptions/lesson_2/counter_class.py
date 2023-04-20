# Создайте класс Счетчик, у которого есть метод add(), увеличивающий значение внутренней int переменной на 1.
# Сделайте так, чтобы с объектом такого типа можно было работать в блоке try-with-resources.
# Подумайте, что должно происходить при закрытии этого ресурса? Напишите метод для проверки, закрыт ли ресурс.
# При попытке вызвать add() у закрытого ресурса, должен выброситься IOException
class IOException(Exception):
    pass


class Counter:
    __open = False

    def __init__(self):
        self.__count = 0

    def open(self):
        self.__open = True

    def add(self):
        if not self.__open:
            raise IOException('open with context-manager')
        self.__count += 1
        return self.count

    @property
    def count(self):
        return self.__count

    def __enter__(self):
        self.__open = True
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print("\nExecution type:", exc_type)
            print("\nExecution value:", exc_val)
            print("\nTraceback:", exc_tb)
        self.__open = False


def main():
    ctr = Counter()

    with ctr:
        for i in range(5):
            print(ctr.add())

    try:
        print(ctr.add())
    except IOException as e:
        print(e)


if __name__ == '__main__':
    main()
