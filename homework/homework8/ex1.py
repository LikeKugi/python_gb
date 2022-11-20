#  В каждой группе учится от 20 до 30 студентов. По итогам экзамена все оценки
# заносятся в таблицу. Каждой группе отведена своя строка. Определите группу с
# наилучшим средним баллом.
from random import randint as RI


def create_marks(n: int) -> list[list]:
    groups = []
    for _ in range(n + 1):
        m = RI(20, 30)
        groups.append([RI(50, 100) for i in range(m + 1)])
    return groups


def find_max_average(groups: list[list]) -> int:
    return groups.index(max(groups, key=lambda x: sum(x) / len(x)))


def main():
    count = int(input('how many groups are there? '))
    groups = create_marks(count)
    print('all markss in groups:')
    print(*groups, sep='\n')
    print('the best group is:')
    best_average = find_max_average(groups)
    print(best_average)


if __name__ == '__main__':
    main()
