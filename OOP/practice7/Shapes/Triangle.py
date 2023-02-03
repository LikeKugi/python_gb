import math

from .Shape import Shape


class Triangle(Shape):

    def __init__(self, a: float, b: float, deg: int):
        self.a = a
        self.b = b
        self.degree = deg

    def get_square(self):
        return self.a * self.b * math.sin(self.degree) / 2

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, value):
        if self.validate(value):
            self.__a = value
        else:
            self.__a = 1

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, value):
        if self.validate(value):
            self.__b = value
        else:
            self.__b = 1

    @property
    def degree(self):
        return self.__degree

    @degree.setter
    def degree(self, value):
        if self.validate(value) and value < 180:
            self.__degree = value
        else:
            self.__degree = 60
