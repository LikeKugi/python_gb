from abc import ABC, abstractmethod


class Shape(ABC):
    name: str = 'figure'

    @abstractmethod
    def get_square(self):
        raise NotImplementedError

    @staticmethod
    def validate(value):
        return (type(value) in (int, float)) and value > 0

