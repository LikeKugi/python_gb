# Создайте скрипт func и функцию чтения
# последней строки файла. Вызовите её из скрипта
# example.


def read_last_line():
    with open('file.txt', 'r', encoding='utf-8') as inf:
        print(inf)  # info about file
        line = inf.readlines()[-1]
    print(line)

