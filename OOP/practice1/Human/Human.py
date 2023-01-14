from typing import TypeVar, Generic

_T_co = TypeVar('_T_co', covariant=True)


class Human:
    def __init__(self, name: str, surname: str, patronymic: str, age: int) -> None:
        self.name = name.capitalize()
        self.surname = surname.capitalize()
        self.patronymic = patronymic.capitalize()
        self.age = age

    def marriage(self, pair: Generic[_T_co]):
        raise NotImplemented

    def create_kid(self, kid: Generic[_T_co]):
        raise NotImplemented

    def set_parents(self, father, mother):
        raise NotImplemented
