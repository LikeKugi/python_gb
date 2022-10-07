"""
Напишите программу, которая по заданному номеру четверти,
показывает диапазон возможных координат точек в этой четверти (x и y).
"""
coordinates = {1: 'x > 0; y > 0', 2: 'x < 0; y > 0', 3: 'x < 0; y < 0', 4: 'x > 0, y < 0'}


def get_int_number(): return int(input())


def print_coordinates(quarter_number: int):
    """
    print avaiable values for X and Y in the quadrant
    :param quarter_number: int
    :return: None
    >>> print_coordinates(1)
    x > 0; y > 0
    >>> print_coordinates(2)
    x < 0; y > 0
    >>> print_coordinates(3)
    x < 0; y < 0
    >>> print_coordinates(4)
    x > 0, y < 0
    >>> print_coordinates(0)
    No such quadrant
    >>> print_coordinates(5)
    No such quadrant
    """
    print(coordinates.get(quarter_number, 'No such quadrant'))


def main():
    quadrant_number = get_int_number()
    print_coordinates(quadrant_number)


if __name__ == '__main__':
    main()
