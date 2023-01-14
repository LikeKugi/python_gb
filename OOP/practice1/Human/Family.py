from typing import TypeVar, Generic

_T_co = TypeVar('_T_co', covariant=True)


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
        self.wife.surname = self.husband.surname

    def make_kids(self, kid: Generic[_T_co]):
        for person in [self.wife, self.husband]:
            person.create_kid(kid)

        kid.set_parents(self.husband, self.wife)

        self.kids.append(kid)

    def _children(self):
        inherits = ' | '.join([str(kid) for kid in self.kids])
        return inherits or 'null'

    def __str__(self):
        return f'{self.husband} + {self.wife} = {self._children()}'
