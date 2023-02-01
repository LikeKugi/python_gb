from .descriptors import PassportDesc, CabinetDesc, NameDesc, SalaryDesc, PhoneDesc


class Worker:
    passport_id = PassportDesc()
    name = NameDesc()
    last_name = NameDesc()
    salary = SalaryDesc()
    phone_number = PhoneDesc()
    cabinet = CabinetDesc()

    def __init__(self, *, name: str = '', last_name: str = '', salary: int = 0, passport_id: int = 0,
                 phone_number: int = 0, cabinet: int = 0):
        self.cabinet = cabinet
        self.phone_number = phone_number
        self.passport_id = passport_id
        self.salary = salary
        self.last_name = last_name
        self.name = name

    def toJSON(self):
        return {"name": self.name,
                "last_name": self.last_name,
                "salary": self.salary,
                "passport": self.passport_id,
                "phone": self.phone_number,
                "cabinet": self.cabinet}

    def __repr__(self):
        return f"""{self.__class__.__name__}({self.name}, {self.last_name},  {self.passport_id}, {self.phone_number}, {self.cabinet})"""


if __name__ == '__main__':
    w1 = Worker()
    print(w1)

