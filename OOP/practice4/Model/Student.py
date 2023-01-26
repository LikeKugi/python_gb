from __future__ import annotations
from datetime import datetime
from typing import TYPE_CHECKING

from .User import User

if TYPE_CHECKING:
    from .Klass import Klass


class Student(User):
    _year: int
    _klass: Klass | None = None

    def __init__(self, *, id: int, name: str, year: int, lessons: list[str] | None = None):
        super().__init__(id, name)
        self.year = year
        if lessons:
            self.grades: dict[str, int | None] = {lesson: None for lesson in lessons}
        else:
            self.grades = {}

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        current_year = datetime.today().year
        if type(value) == int and (1900 < value <= current_year):
            self._year = value
        else:
            raise TypeError(f'{value} should be type of int and 1900 < {value} <= {current_year}')

    @property
    def klass(self):
        return self._klass

    @klass.setter
    def klass(self, value):
        self._klass = value

    def add_lesson(self, value):
        if self.check_for_str(value):
            self.grades.setdefault(value, None)

    def get_grade(self, lesson: str, grade: int):
        if self.check_for_str(lesson) and isinstance(grade, int) and 0 <= grade <= 5:
            self.grades[lesson] = grade
        else:
            raise TypeError(f'{grade} should be instance of int and 0 <= {grade} <= 5')

    def toJSON(self):
        return {
            'id': self.id,
            'name': self.name,
            'year': self.year,
            'grades': self.grades
        }

    def __eq__(self, other: Student) -> bool:
        if type(other) == Student:
            return (self.id == other.id and self.name == other.name
                    and self.year == other.name and self.grades == other.grades)
        raise NotImplemented

    def __lt__(self, other: Student) -> bool:
        if type(other) == Student:
            return (self.grades < other.grades) and (self.name != other.name)
        raise NotImplemented

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.id}, {self.name}, {self.year}, {self.grades})'
