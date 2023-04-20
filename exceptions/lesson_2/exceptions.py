# Создайте класс исключения, который будет выбрасываться при делении на 0.
# Исключение должно отображать понятное для пользователя сообщение об ошибке.

# Создайте класс исключений, которое будет возникать при обращении к пустому элементу в массиве ссылочного типа.
# Исключение должно отображать понятное для пользователя сообщение об ошибке

# Создайте класс исключения, которое будет возникать при попытке открыть несуществующий файл.
# Исключение должно отображать понятное для пользователя сообщение об ошибке.

class CustomZeroDivisionError(ArithmeticError):
    def __init__(self):
        self.message = 'Zero division error'

    def __str__(self):
        return self.message


class NoneElementArrayException(Exception):
    def __init__(self, msg='None element in array'):
        self.message = msg

    def __str__(self):
        return self.message


def test_zero():
    a = 3
    b = 0
    try:
        print(a / b)
    except ZeroDivisionError:
        raise CustomZeroDivisionError


def test_none():
    arr = [1, 2, 3, None, 4, 5]
    for i, el in enumerate(arr):
        if el is None:
            raise NoneElementArrayException(f'{i} element is None')


def main():
    try:
        test_zero()
    except CustomZeroDivisionError as e:
        print(e)

    try:
        test_none()
    except NoneElementArrayException as e:
        print(e)


if __name__ == '__main__':
    main()
