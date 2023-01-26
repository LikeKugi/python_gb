from .loader import load_data
from data import create_file

PATH_KLASSES = 'storage/klasses.bin'

def update_student(student: dict):
    klass = load_data(PATH_KLASSES)

    res_id = int(student['id'])

    res_grades = student['grades']

    current = klass.students.get(res_id)


    if student.get('name'):
        current.name = student.get('name')

    for lesson, grade in res_grades.items():
        print(lesson, grade, type(grade))
        current.get_grade(lesson, int(grade))

    klass.append(current)
    create_file(klass, path=PATH_KLASSES)