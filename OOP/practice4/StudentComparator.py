from service import create_random_klass, create_student, add_student_to_klass


if __name__ == '__main__':
    for _ in range(1):
        create_random_klass()

    for _ in range(10):
        student = create_student()
        print(student)
        add_student_to_klass(student)