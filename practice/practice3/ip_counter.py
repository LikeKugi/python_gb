# Имеется список ip-адресов посетителей сайта. Определите, какой процент посетителей заходил на сайт более 1 раза.

from random import randrange as rr


def generate_ip():
    return ('.'.join([str(rr(0, 256)) for _ in range(4)]))


def create_ip_list():
    visitors = list()
    for _ in range(50000):
        visitors.append(generate_ip())
    return visitors


def find_duplicates(visitors):
    counts = {}
    for visitor in visitors:
        counts[visitor] = counts.setdefault(visitor, 0) + 1
    target_group = len([el for el in counts.values() if el > 1])
    print(target_group)
    total = (target_group / len(counts)) * 100
    print(total)


def main():
    vitors_list = create_ip_list()
    find_duplicates(vitors_list)


if __name__ == '__main__':
    main()
