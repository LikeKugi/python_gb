from abc import ABC, abstractmethod


class Animal(ABC):
    name: str = ''
    age: int = 0

    @abstractmethod
    def say(self):
        pass

    def __str__(self):
        return f'{self.name}: {self.age}'


class Dog(Animal):
    def __init__(self, name, age):
        self.age = age
        self.name = name

    def say(self):
        print('wooow')


class Cat(Animal):
    def __init__(self, name, age):
        self.age = age
        self.name = name

    def say(self):
        print('Mew')


if __name__ == '__main__':
    my_dog = Dog('Sharik', 5)
    my_cat = Cat('Matroskin', 6)

    for pet in [my_cat, my_dog]:
        pet.say()
