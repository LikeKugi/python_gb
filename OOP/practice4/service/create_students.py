import names

from Model import Student
from data import create_file, read_file

LESSONS = ('Math', 'Computer Science', 'Algorithms')
PATH_KLASSES = 'storage/klasses.bin'


def _load_students(path=PATH_KLASSES):
    try:
        students = read_file(path=path).students
    except FileNotFoundError:
        students = {}
    return students


def _create_new_student(*, id: int = 0, name: str | None = None, year: int = 2001, lessons=LESSONS):
    if not name:
        name = names.get_first_name(gender='male')
    _student = Student(id=id, name=name, year=year, lessons=lessons)
    return _student


def create_student_list(unit: Student, students: list | None = None, path=PATH_KLASSES):
    if not students:
        students = _load_students(path=path)
    students.append(unit)
    create_file(students, path=path)


def create_student(*, path=PATH_KLASSES, id: int | None = None, name=None, year=2001, lessons=LESSONS):
    if not id:
        students = _load_students(path=path)
        if students:
            id = list(students.keys())[-1] + 1
        else:
            id = 0
    print(f'{id = }; {id = }')
    _student = _create_new_student(id=id, name=name, year=year, lessons=lessons)

    return _student
