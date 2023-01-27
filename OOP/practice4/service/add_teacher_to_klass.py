from data import create_file, read_file

PATH_KLASSES = 'storage/klasses.bin'


def add_teacher_to_klass(teacher, path=PATH_KLASSES):
    klass = read_file(path=path)
    klass.add_teacher(teacher)
    create_file(klass, path=path)