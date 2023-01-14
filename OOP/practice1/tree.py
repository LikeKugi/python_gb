from __future__ import annotations
from typing import TypeVar
from random import randint as ri

import names

from Human import Man, Woman, Family

_T_co = TypeVar('_T_co', covariant=True)


def main():
    families: list[Family] = []

    man = create_man(age=1400)
    woman = create_pair(man)
    _family = create_family(man, woman)

    print(f'{_family}')

    families.append(_family)

    i = 0
    while families[i].husband.age < 1500:
        families.extend(create_families_kids(families[i]))
        i += 1

    # for i in range(30):
    #     families.extend(create_families_kids(families[i]))
    write_families(families)

    for family in families:
        print(f'{family}')

    egg = create_man()
    print(f'{egg = }')


def create_man(*, name=None, surname=None, patronymic=None, age=None):
    _age = age or ri(1960, 2004)
    _name = name or names.get_first_name(gender='male')
    _surname = surname or names.get_last_name()
    _patronymic = patronymic or names.get_first_name(gender='male')
    man = Man(_name, _surname, _patronymic, _age)
    return man


def create_woman(*, name=None, surname=None, patronymic=None, age=None):
    _age = age or ri(1960, 2004)
    _name = name or names.get_first_name(gender='female')
    _surname = surname or names.get_last_name()
    _patronymic = patronymic or names.get_first_name(gender='female')
    woman = Woman(_name, _surname, _patronymic, _age)
    return woman


def create_kid(person_1, person_2):
    if type(person_1) == Man:
        man = person_1
        woman = person_2
    else:
        man = person_2
        woman = person_1
    _age = min(man.age, woman.age) + ri(18, 27)
    sex = ri(0, 1)
    if sex:
        kid = create_man(age=_age, surname=man.surname, patronymic=man.name)
    else:
        kid = create_woman(age=_age, surname=man.surname, patronymic=man.name)
    return kid


def create_pair(person):
    if type(person) == Man:
        pair = create_woman(age=(person.age + ri(-5, 5)))
    else:
        pair = create_man(age=(person.age + ri(-5, 5)))
    return pair


def create_families_kids(family: Family):
    _families: list[Family] = []
    for kid in family.kids:
        pair = create_pair(kid)
        _family = create_family(kid, pair)
        _families.append(_family)
    return _families


def create_family(man, woman):
    _family = Family(man, woman)
    for _ in range(ri(0, 5)):
        kid = create_kid(man, woman)
        _family.make_kids(kid)
    print(_family)
    return _family


def write_families(families: list[Family]):
    with open('families.txt', 'w', encoding='utf-8') as ouf:
        for _family in families:
            print(_family, file=ouf)


if __name__ == '__main__':
    main()
