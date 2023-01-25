from __future__ import annotations

import names

from Model import Teacher
from data import create_file, read_file

PATH_TEACHERS = 'storage/teachers.bin'


def create_teacher(*, id: int = 0, name: str | None = None, lesson='Math'):
    if not name:
        name = names.get_first_name(gender='male')
    joe = Teacher(id=id, name=name, lesson=lesson)
    print(joe)
    return joe


def create_teacher_list(unit: Teacher, path=PATH_TEACHERS):
    try:
        teachers: list = read_file(path=path)
    except FileNotFoundError:
        teachers = []
    teachers.append(unit)
    create_file(teachers, path=path)
