# Запишите в файл следующие строки:
# Анна=4
# Елена=5
# Марина=6
# Владимир=?
# Константин=?
# Иван=4
# Реализуйте метод, который считывает данные из файла и сохраняет в двумерный массив
# (либо HashMap, если студенты с ним знакомы).
# В отдельном методе нужно будет пройти по структуре данных, если сохранено значение ?,
# заменить его на соответствующее число.
# Если на каком-то месте встречается символ, отличный от числа или ?,
# бросить подходящее исключение.Записать в тот же файл данные с замененными символами ?.

import json
import re


def write_to_file(data: str):
    with open('students.log', 'a') as ouf:
        print(data, file=ouf)


def read_from_file():
    try:
        with open('students.log', 'r') as inf:
            lines = inf.read().split('\n')
            return lines
    except Exception as e:
        print(e)
    return False


def parse_data(data:list[str]) -> dict:
    pattern = re.compile('[0-9]+')
    out = {}
    for line in data:
        if not line:
            continue
        name, grade = line.split('=')
        if grade == '?':
            grade = 3
        elif not re.match(pattern, grade):
            raise ValueError(f'{grade} must be in [?0-9]')
        out[name] = grade
    return out


def to_json(data:dict) -> None:
    with open('data.json', 'w') as ouf:
        json.dump(data, ouf)


def main():
    write_to_file(f'Анна=4\nЕлена=5\nМарина=6\nВладимир=?\nКонстантин=?\nИван=4')
    data = read_from_file()
    print(data)
    if data:
        data_dict = parse_data(data)
        to_json(data_dict)


if __name__ == '__main__':
    main()

