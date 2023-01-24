class User:
    id: int
    _name: str

    def __init__(self, id: int, name: str):
        if type(id) == int:
            self.id = id
        else:
            raise TypeError(f'{id} should be int')

        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if self.check_for_str(value):
            self._name = value

    @staticmethod
    def check_for_str(value) -> bool:
        if isinstance(value, str):
            return True
        else:
            raise TypeError(f'{value} should be type of str')