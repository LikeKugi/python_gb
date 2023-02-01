class SalaryDesc:
    def __set_name__(self, owner, name):
        self.private_name = f'_{name}'

    def __get__(self, instance, owner):
        value = getattr(instance, self.private_name)
        return value

    def __set__(self, instance, value):
        if isinstance(value, float) and 0 < value < 1_000_000:
            setattr(instance, self.private_name, value)
        else:
            setattr(instance, self.private_name, 0)