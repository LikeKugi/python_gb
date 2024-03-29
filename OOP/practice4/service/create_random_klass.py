from typing import TYPE_CHECKING

from .create_students import create_student
from .create_teachers import create_teacher, create_teacher_list

from Model import Klass
from data import create_file, read_file

if TYPE_CHECKING:
    from ..Model import Klass

YEAR = 2022

LESSONS = ('Math', 'Computer Science', 'Algorithms')
PATH_KLASSES = 'storage/klasses.bin'


def create_random_klass(*, year=YEAR, lessons=LESSONS):
    klass = Klass(year)

    for i in range(15):
        if klass.students:
            _id = list(klass.students.keys())[-1] + 1
        else:
            _id = 0
        student = create_student(id=_id, year=year, lessons=LESSONS)
        klass.append(student)

    teachers = []
    for lesson in lessons:
        teacher = create_teacher(lesson=lesson)
        teachers.append(teacher)
        create_teacher_list(teacher)
        klass.create_lesson(lesson, teacher)
        teacher.add_klass(klass)

    klass.study()

    create_klass_list(klass=klass)


def create_klass_list(klass: Klass, path=PATH_KLASSES):
    create_file(klass, path=path)
