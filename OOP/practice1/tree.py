from __future__ import annotations
from typing import TypeVar
from random import randint as ri

import names

from Human import Man, Woman, Family

# Human covariant Man | Woman
_T_co = TypeVar('_T_co', covariant=True)

OLDEST_AGE = 1400
GENERATIONS = 7


def main():
    families: list[list[Family]] = []

    man = create_man(age=OLDEST_AGE)
    woman = create_pair(man)
    _family = create_family(man, woman, kid_min=3)

    print(f'{_family = }')

    families.append([_family])

    i = 0

    for _row in families:
        generation = []
        for _element in _row:
            if _element.kids:
                generation.extend(create_families_kids(_element))
        families.append(generation)
        i += 1

        if i == GENERATIONS:
            break

    print(*families, sep='\nGeneration -->')

    write_families(families)


def create_man(*, name=None, surname=None, patronymic=None, age=None) -> Man:
    """
    Create male of given paramethers or random
    @param name: str
        Name of the man (given or random)
    @param surname: str
        Surname of the man (given or random)
    @param patronymic: str
        Patronymic of the man (given or random)
    @param age: int
        Age of birth (given or random between [1960; 2004])
    @return: Man
    """
    _age = age or ri(1960, 2004)
    _name = name or names.get_first_name(gender='male')
    _surname = surname or names.get_last_name()
    _patronymic = patronymic or names.get_first_name(gender='male')
    man = Man(_name, _surname, _patronymic, _age)
    return man


def create_woman(*, name=None, surname=None, patronymic=None, age=None) -> Woman:
    """
    Create female of given paramethers or random
    @param name: str
        Name of the man (given or random)
    @param surname: str
        Surname of the man (given or random)
    @param patronymic: str
        Patronymic of the man (given or random)
    @param age: int
        Age of birth (given or random between [1960; 2004])
    @return: Woman
    """
    _age = age or ri(1960, 2004)
    _name = name or names.get_first_name(gender='female')
    _surname = surname or names.get_last_name()
    _patronymic = patronymic or names.get_first_name(gender='female')
    woman = Woman(_name, _surname, _patronymic, _age)
    return woman


def create_kid(person_1: _T_co, person_2: _T_co) -> _T_co:
    """
    Create a kid of the pair
    @param person_1: _T_co [Man | Woman]
        First person in the Family
    @param person_2: _T_co [Man | Woman]
        Second person in the Family
    @return: _T_co [Man | Woman]
        A kid that can be a child of the family
    """
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


def create_pair(person: _T_co) -> _T_co:
    """
    Create an invariant pair for the person
    @param person: _T_co [Man | Woman]
        the person
    @return: _T_co [Man | Woman]
        invariant sex of the person Human covariant typed
    """
    min_age = -5
    max_age = 5
    if type(person) == Man:
        pair = create_woman(age=(person.age + ri(min_age, max_age)))
    else:
        pair = create_man(age=(person.age + ri(min_age, max_age)))
    return pair


def create_families_kids(family: Family) -> list[Family]:
    """
    Creates list of families with the kids of given Family and random
    invariant Human covariant typed
    @param family: Family
        Man, Woman, list[_T_co]: kids
    @return: list[Family]
        list of families
    """
    _families: list[Family] = []
    for kid in family.kids:
        pair = create_pair(kid)
        _family = create_family(kid, pair)
        _families.append(_family)
    return _families


def create_family(man, woman, *, kid_min=0, kid_max=5):
    _family = Family(man, woman)
    for _ in range(ri(kid_min, kid_max)):
        kid = create_kid(man, woman)
        _family.make_kids(kid)
    print(f'Created: {_family}')
    return _family


def write_families(families: list[list[Family]]):
    with open('families.txt', 'w', encoding='utf-8') as ouf:
        for i, _generation in enumerate(families):
            print(f'\nGENERATION {i}\n', file=ouf)
            for _family in _generation:
                print(_family, file=ouf)


if __name__ == '__main__':
    main()
