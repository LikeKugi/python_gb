def sum_of_two(a: int, b: int) -> int:
    """
    returns sum of two int numbers
    :param a: int
        first number
    :param b: int
        second number
    :return: int
        a + b
    """
    return a + b


def get_int(*args: str | None) -> int: return int(input(*args))


def main():
    """
    sum of two elements
    :return: None
    """
    x = get_int('x = ')
    y = get_int('y = ')
    total = sum_of_two(x, y)
    print(f'sum of {x} + {y} = {total}')


if __name__ == '__main__':
    print(locals())
    main()
