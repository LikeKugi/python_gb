from Animal import Cat, Dog, Animal


class Human(Animal):

    def __init__(self, name, age):
        self.age = age
        self.name = name
        self._pets = []

    def say(self):
        print('Я король мира!!!!')

    @property
    def pets(self):
        return ' '.join([str(el) for el in self._pets])

    @pets.setter
    def pets(self, value):
        if type(value) in {Cat, Dog}:
            self._pets.append(value)
        else:
            raise NotImplemented

    def set_pet(self):
        _choose = int(input('0: dog, 1: cat '))
        if _choose in {0, 1}:
            _name = input('whats name: ').capitalize()
            _age = int(input('Whats age: '))
            if _choose:
                pet = Cat(_name, _age)
            else:
                pet = Dog(_name, _age)
            self.pets = pet

    def __str__(self):
        return f""" I am {self.name}
        I am {self.age} y.o.
        I have {self.pets}
        """


if __name__ == '__main__':
    bob = Human('Bob', 18)
    bob.set_pet()
    print(bob)
