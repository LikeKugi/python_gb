# Найдите все числа до 10000, у который
# количество делителей равно 10


def check_number(n):
    """
    create list of divigers
    :param n: int
    :return: bool
    """
    divigers = list()
    for diviger in range(1, int(n ** 0.5)):
        if n % diviger == 0:
            divigers.append(diviger)
    return len(divigers) == 5


def find_numbers():
    """
    check numbers
    :return: list
    """
    numbers = list()
    for i in range(1, 10_001):
        if check_number(i):
            numbers.append(i)
    return numbers


def main():
    print(find_numbers.__doc__)
    print(check_number.__doc__)
    print(*find_numbers())


if __name__ == '__main__':
    main()