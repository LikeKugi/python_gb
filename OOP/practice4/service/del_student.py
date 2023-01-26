from data import create_file, read_file

PATH_KLASSES = 'storage/klasses.bin'


def del_student(id_student, path=PATH_KLASSES):
    klass = read_file(path=path)
    del klass.students[id_student]
    create_file(klass, path=path)
