from __future__ import annotations
from .User import User
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .Klass import Klass


class Teacher(User):

    def __init__(self, id: int, name: str, lesson: str):
        super().__init__(id, name)
        if self.check_for_str(lesson):
            self.lesson = lesson
        self.klasses: list[Klass] = []

    def add_klass(self, klass: Klass):
        return self.klasses.append(klass)

    def __eq__(self, other: Teacher) -> bool:
        if type(other) == Teacher:
            return (self.id == other.id and self.name == other.name
                    and self.lesson == other.lesson and self.klasses == other.klasses)
        raise NotImplemented

    def __lt__(self, other: Teacher) -> bool:
        if type(other) == Teacher:
            return (self.id < other.id) and (self.name != other.name) and (self.klasses != other.klasses)
        raise NotImplemented

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.id}, {self.name}, {self.lesson})'
