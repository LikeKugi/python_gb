class PassportDesc:
    def __set_name__(self, owner, name):
        self.private_name = f'_{name}'

    def __get__(self, instance, owner):
        value = getattr(instance, self.private_name)
        return value

    def __set__(self, instance, value):
        if type(value) == int and 1 < value < 1000000:
            setattr(instance, self.private_name, value)
        elif value.isdigit():
            setattr(instance, self.private_name, int(value))
        else:
            setattr(instance, self.private_name, 0)