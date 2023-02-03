from .Shape import Shape


class Square(Shape):

    def __init__(self, a: float):
        self.side = a

    def get_square(self):
        return self.side ** 2

    @property
    def side(self):
        return self.__side

    @side.setter
    def side(self, value):
        if self.validate(value):
            self.__side = value
        else:
            print(f'{value} should be type of int or float')
            self.__side = 1

