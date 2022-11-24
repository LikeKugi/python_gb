from random import randint as RI


class QuizNumber:
    __slots__ = ['_number']
    _instance = None
    counter = 0

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.number = RI(0, 1000)
        self.__class__.counter = 0

    def __str__(self):
        return f'Было загадано число {self.number}'

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        if type(value) == int and 0 < value < 1000:
            self._number = value
        else:
            raise ValueError(f'{value} is prohibited for this quiz')

    @classmethod
    def increase_counter(cls):
        cls.counter += 1

    def check(self, value):
        if type(value) != int:
            raise ValueError('Should be integer number')
        elif value == self._number:
            return f'Верно!, Вы угадали число с {self.counter + 1} попытки'
        elif value < self._number:
            self.increase_counter()
            return f'{value} меньше загаданного числа'
        elif value > self._number:
            self.increase_counter()
            return f'{value} больше загаданного числа'
