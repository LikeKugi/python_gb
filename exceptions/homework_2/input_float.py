# Реализуйте метод, который запрашивает у пользователя ввод дробного числа (типа float),
# и возвращает введенное значение. Ввод текста вместо числа не должно приводить к падению приложения,
# вместо этого, необходимо повторно запросить у пользователя ввод данных.


def input_float():
    while True:
        line = input('enter float number or "q" to exit: ')
        try:
            if line == 'q':
                return
            line = float(line)
            yield line
        except ValueError:
            print('plz enter float number')


def main():
    query = input_float()
    for _ in query:
        number = next(query)
        print(number)


if __name__ == '__main__':
    main()
