"""
Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

Пример:

- A (3,6); B (2,1) -> 5,09
- A (7,-5); B (1,-1) -> 7,21
"""


def get_tuple_float_numbers(): return tuple(float(el) for el in input('enter (x y) coordinates: ').split())


def find_range_between_points(a, b):
    """
    find range between 2 points a(a[0],a[1]) and b(b[0],b[1]) on the coordinate plane
    :param a: tuple(float,float)
    :param b: tuple(float,float)
    :return: float
    >>> find_range_between_points((3,6), (2,1))
    5.099
    >>> find_range_between_points((7,-5), (1,-1))
    7.211
    """
    return round(((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5, 3)


def main():
    a_point = get_tuple_float_numbers()
    b_point = get_tuple_float_numbers()
    range_between = find_range_between_points(a_point, b_point)
    print(range_between)


if __name__ == '__main__':
    main()
