import names

from Model import Student
from data import create_file, read_file

LESSONS = ('Math', 'Computer Science', 'Algorithms')
PATH_STUDENTS = 'storage/students.bin'


def _load_students(path=PATH_STUDENTS):
    try:
        students: list = read_file(path=path)
    except FileNotFoundError:
        students = []
    return students


def _create_new_student(*, id: int = 0, name: str | None = None, year: int = 2001, lessons=LESSONS):
    if not name:
        name = names.get_first_name(gender='male')
    _student = Student(id=id, name=name, year=year, lessons=lessons)
    return _student


def create_student_list(unit: Student, students: list | None = None, path=PATH_STUDENTS):
    if not students:
        students = _load_students(path=path)
    students.append(unit)
    create_file(students, path=PATH_STUDENTS)


def create_student(*, path=PATH_STUDENTS, name=None, year=2001, lessons=LESSONS):
    students = _load_students(path=path)
    _id = len(students)
    _student = _create_new_student(id=_id, name=name, year=year, lessons=lessons)
    create_student_list(_student, students)

    return _student
