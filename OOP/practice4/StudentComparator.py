from __future__ import annotations
import names





class StudentComparator:

    @staticmethod
    def compare(unit_1: Student, unit_2: Student) -> int:
        if type(unit_1) != Student or type(unit_2) != Student:
            raise NotImplemented
        if unit_1 > unit_2:
            return 1
        elif unit_1 < unit_2:
            return -1
        return 0

    @staticmethod
    def sort(unit: Student) -> int:
        if type(unit) == Student:
            return unit.grade
        else:
            return unit.__hash__()


if __name__ == '__main__':
    student1 = Student('Joe', 1)
    student2 = Student('Doe', 2)
    compare = StudentComparator()

    student3 = Student('Joe', 1)

    print(compare.compare(student1, student2))
    print(compare.compare(student1, student3))

    students = []

    for i in range(10):
        students.append(Student(names.get_first_name(gender='male'), i))

    students.append('fen')
    students.append(123)
    students.extend([1, 4, 14, 42])

    print(sorted(students, key=lambda x: compare.sort(x), reverse=True))
