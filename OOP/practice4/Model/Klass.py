from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .Teacher import Teacher
    from .Student import Student


class Klass:

    def __init__(self, year):
        self.year = year
        self.students: dict[int, 'Student'] = {}
        self.lessons: dict[str, Teacher] = {}
        self.teachers: list[Teacher] = []

    def create_lesson(self, lesson, teacher: 'Teacher') -> None:
        if self.check_for_str(lesson):
            self.lessons.setdefault(lesson, teacher)
        self.teachers.append(teacher)
        teacher.add_klass(self)

    def append(self, unit: 'Student') -> None:
        self.students.update({unit.id: unit})
        unit.klass = self
        if self.lessons:
            self.add_student_lessons(unit)

    def study(self):
        for index, student in self.students.items():
            self.add_student_lessons(student)
            print(student.grades)

    def add_student_lessons(self, unit: 'Student'):
        for lesson in self.lessons:
            unit.add_lesson(lesson)

    @staticmethod
    def check_for_str(value) -> bool:
        if isinstance(value, str):
            return True
        else:
            raise TypeError(f'{value} should be type of str')

    def __repr__(self):
        return f'{self.year}, \n\t{[(s_id, student) for s_id, student in self.students.items()]}, \n\t\t{[lesson for lesson in self.lessons]}'
