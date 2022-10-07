"""
Напишите программу, которая принимает на вход координаты точки (X и Y),
причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
в которой находится эта точка (или на какой оси она находится).
"""


def get_float_number(): return (float(el) for el in input().split())


def check_quadrant(x, y):
    """
    print number of coordinate quadrants by coordinates of the point
    neither X not Y in A(X,Y) shouldn't be 0
    :param x: float
    :param y: float
    :return: None
    >>> check_quadrant(1,1)
    1
    >>> check_quadrant(-1,1)
    2
    >>> check_quadrant(-1,-1)
    3
    >>> check_quadrant(1,-1)
    4
    >>> check_quadrant(34,-30)
    4
    >>> check_quadrant(2,4)
    1
    >>> check_quadrant(-34,-30)
    3
    """
    assert (x != 0 and y != 0), print("the point shouldn't be on the coordinates axes")
    if x > 0:
        if y > 0:
            print(1)
        else:
            print(4)
    else:
        if y > 0:
            print(2)
        else:
            print(3)


def main():
    x, y = get_float_number()
    check_quadrant(x, y)


if __name__ == '__main__':
    main()
