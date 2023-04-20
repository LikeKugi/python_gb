# Дан следующий код, исправьте его там, где требуется

def main():
    a = 90
    b = 3
    print(a / b)
    try:
        print_sum(a, b)
    except FileNotFoundError as e:
        print(e)

    try:
        abc = [1, 2]
        abc[3] = 9
    except IndexError as e:
        print(e)


def print_sum(a, b):
    raise FileNotFoundError(a + b)


if __name__ == '__main__':
    main()
