from typing import TypeVar, Generic

from .Human import Human

_T = TypeVar('_T')


class Man(Human):
    sex = 'male'

    def __init__(self, name, surname, patronymic, age):
        super().__init__(name, surname, patronymic, age)
        self.wife = None
        self.kids = []
        self.parents = None

    def marriage(self, pair: Generic[_T]):
        self.wife: _T = pair

    def create_kid(self, kid: Generic[_T]):
        self.kids.append(kid)

    def set_parents(self, father: Generic[_T], mother: Generic[_T]):
        self.parents = (father, mother)

    def __str__(self):
        return f'{self.name} {self.surname} {self.patronymic} {self.age}'

    def __repr__(self):
        return f'Man({self.name}, {self.surname}, {self.patronymic}, {self.age})'