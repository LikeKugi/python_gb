from data import create_file, read_file

PATH_KLASSES = 'storage/klasses.bin'


def add_student_to_klass(student, path=PATH_KLASSES):
    klass = read_file(path=path)
    klass.append(student)
    create_file(klass, path=path)
