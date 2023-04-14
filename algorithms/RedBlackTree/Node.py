import enum
from typing import TypeVar, Literal

_T = TypeVar('_T', bound='Node')


class Colors(enum.IntEnum):
    red = 1
    black = 2


class Node:

    def __init__(self: _T, data, color=1):
        """
        Node
        Colors:
            1 - red

            2 - black
        :param data: any
        """
        self.data = data
        self.parent: _T | None = None
        self.left: _T | None = None
        self.right: _T | None = None
        self.color = 1

    def __repr__(self: _T):
        return f'Node({self.data}) Color: {self.color}'

    @property
    def color(self: _T):
        return Colors(self.__color).name

    @color.setter
    def color(self: _T, value: Literal[1, 2]):
        if value in set(map(int, Colors)):
            self.__color = value
        else:
            raise NotImplementedError(f'No such color available ({value})')

    def color_value(self):
        return self.__color


if __name__ == '__main__':
    node = Node(5)
    print(node)
