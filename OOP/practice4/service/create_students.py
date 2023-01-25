from __future__ import annotations
from Model import Student
import names


def create_student():
    joe = Student(id=0, name=names.get_first_name(gender='male'), year=2001 )
    print(joe)
