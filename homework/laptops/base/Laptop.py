from typing import TypeVar

_T = TypeVar('_T', int, float)
_ST = TypeVar('_ST', int, float, str)


def to_digit(value: _ST) -> _T:
    """
    returns the number of memory
    :param value: str | float | int
    :return: float | int
    """
    if type(value) in (int, float):
        return value
    out = 0
    for char in value:
        if not (char.isdigit() or char in '.'):
            value = value.replace(char, '')
    try:
        if value and '.' in value:
            out = float(value)
        else:
            out = int(value)
    except ValueError:
        print(f'{value} should be int or float')
    finally:
        return out


class Memory:
    """
    Memory storage and ram descriptor class
    """

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.name] or None

    def __set__(self, instance, value):
        instance.__dict__[self.name] = self.get_memory(value)

    @classmethod
    def get_memory(cls, value: _ST) -> _T:
        if type(value) in (int, float):
            return value
        out = 0
        if value.lower().endswith('gb'):
            out = to_digit(value)
        elif value.lower().endswith('tb'):
            out = to_digit(value) * 1024
        return out


class Laptop:
    _price = 0
    ram = Memory()
    storage = Memory()
    _inches = 0
    _screen_property = ''

    def __init__(self, product_name, image, cpu, ram, storage, screen, price):
        self.price = price
        self.screen = screen
        self.storage = storage
        self.ram = ram
        self.cpu = cpu
        self.image = image
        self.product_name = product_name

    def __repr__(self):
        return f'{self.__class__.__name__}({self.product_name!r}, {self.image!r}, {self.cpu!r}, {self.ram!r}, {self.storage!r}, {self.screen!r}, {self.price!r})'

    @property
    def price(self) -> str:
        return self._price

    @price.setter
    def price(self, value: _T):
        self._price = to_digit(value)

    @property
    def screen(self):
        return self._inches

    @screen.setter
    def screen(self, value: str):
        inches, screen_property = value.split(', ')
        self._inches = to_digit(inches)
        self._screen_property = screen_property

    def get_screen_property(self): return f'{self._screen_property}'


if __name__ == '__main__':
    laptop1 = Laptop("Samsung Notebook 9", "samsung-notebook-9.jpg", "Intel Core i7, 8th generation", "16GB", "256GB",
                     "13.9-inch, 3K (3,000 x 2,080)", "1499")
    laptop2 = Laptop(1, 2, 3, "8GB", 5, "15-inch, Retina display", 7)

    for el in (laptop1, laptop2):
        print(el)
