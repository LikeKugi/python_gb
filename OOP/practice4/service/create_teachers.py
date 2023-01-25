from __future__ import annotations
from Model import Teacher
import names


def create_teacher():
    joe = Teacher(id=0, name=names.get_first_name(gender='male'), lesson='Math' )
    print(joe)