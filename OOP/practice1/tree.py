from __future__ import annotations
from typing import TypeVar, Generic, Protocol
from random import randint as ri

_T_co = TypeVar('_T_co', covariant=True)


def main():
    man = Man('John', 'Doe', 'Harry', 19)
    woman = Woman('Marry', 'Olsen', 'Boris', 18)
    family = Family(man, woman)
    family.make_kids('alex')

    for kid in ['alex', 'mary', 'april', 'wednesday']:
        family.make_kids(kid)

    print(f'{family}')

    for person in [man, woman]:
        print(person.kids)


class Human:
    def __init__(self, name: str, surname: str, patronymic: str, age: int) -> None:
        self.name = name.capitalize()
        self.surname = surname.capitalize()
        self.patronymic = patronymic.capitalize()
        self.age = age
        print(self)

    def marriage(self, pair: Generic[_T_co]):
        raise NotImplemented

    def create_kid(self, kid: Generic[_T_co]):
        raise NotImplemented

    def set_parents(self, father, mother):
        raise NotImplemented


class Man(Human):
    sex = 'male'

    def __init__(self, name, surname, patronymic, age):
        super().__init__(name, surname, patronymic, age)
        self.wife = None
        self.kids = []
        self.parents = None

    def marriage(self, pair: Generic[_T_co]):
        self.wife: _T_co = pair

    def create_kid(self, kid: Generic[_T_co]):
        self.kids.append(kid)

    def set_parents(self, father: Generic[_T_co], mother: Generic[_T_co]):
        self.parents = (father, mother)

    def __str__(self):
        return f'{self.name} {self.surname} {self.patronymic} {self.age}'

    def __repr__(self):
        return f'Man({self.name}, {self.surname}, {self.patronymic}, {self.age})'


class Woman(Human):
    sex = 'female'

    def __init__(self, name, surname, patronymic, age):
        super().__init__(name, surname, patronymic, age)
        self.husband = None
        self.kids = []
        self.parents = None

    def marriage(self, pair: Generic[_T_co]):
        self.husband: _T_co = pair

    def create_kid(self, kid: Generic[_T_co]):
        self.kids.append(kid)

    def set_parents(self, father: Generic[_T_co], mother: Generic[_T_co]):
        self.parents = (father, mother)

    def __str__(self):
        return f'{self.name} {self.surname} {self.patronymic} {self.age}'

    def __repr__(self):
        return f'Woman({self.name}, {self.surname}, {self.patronymic}, {self.age})'


class Family:

    def __init__(self, husband: Generic[_T_co], wife: Generic[_T_co]):
        if husband.sex != wife.sex:
            self.husband: _T_co = husband
            self.wife: _T_co = wife
            self.kids: list[_T_co] = []

        else:
            raise NotImplemented

    def marriage(self):
        self.husband.marriage(self.wife)
        self.wife.marriage(self.husband)

    def make_kids(self, name):
        sex = ri(0, 1)
        if sex:
            kid: _T_co = Woman(name, self.husband.surname, self.husband.name, 0)
        else:
            kid: _T_co = Man(name, self.husband.surname, self.husband.name, 0)

        for person in [self.wife, self.husband]:
            person.create_kid(kid)

        kid.set_parents(self.husband, self.wife)

        self.kids.append(kid)

    def _children(self):
        inherits = ''
        for kid in self.kids:
            inherits += f'{kid}'
        return inherits

    def __str__(self):
        return f'{self.husband} + {self.wife} = {self._children()}'


if __name__ == '__main__':
    main()
