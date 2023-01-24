from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .Teacher import Teacher
    from .Student import Student


class Klass:

    def __init__(self, year):
        self.year = year
        self.students: list[Student] = []
        self.lessons: dict[str, Teacher] = {}
        self.teachers: list[Teacher] = []

    def create_lesson(self, lesson, teacher: Teacher) -> None:
        if self.check_for_str(lesson):
            self.lessons.setdefault(lesson, teacher)
        self.teachers.append(teacher)

    def append(self, unit: Student) -> None:
        self.students.append(unit)

    @staticmethod
    def check_for_str(value) -> bool:
        if isinstance(value, str):
            return True
        else:
            raise TypeError(f'{value} should be type of str')

    def __repr__(self):
        return f'{self.year}, \n\t{[student for student in self.students]}, \n\t\t{[lesson for lesson in self.lessons]}'
