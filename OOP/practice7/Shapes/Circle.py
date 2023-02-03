import math

from .Shape import Shape


class Circle(Shape):

    def __init__(self, r: float):
        """

        :type r: float
        """
        self.__radius: float = r

    def get_square(self):
        return 2 * math.pi * self.__radius

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value: int | float):
        if self.validate(value):
            self.__radius = value
        else:
            raise ValueError (f'{value} should bo int or float and > 0')


