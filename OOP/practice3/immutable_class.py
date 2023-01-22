# Попытка создать неизменяемый класс
# Monkey Patching <3

class Doggy:
    __slots__ = ['say', 'name', 'age']

    def __init__(self, say, name, age):
        object.__setattr__(self, 'age', age)
        object.__setattr__(self, 'name', name)
        object.__setattr__(self, 'say', say)

    def __setattr__(self, key, value):
        raise AttributeError('Can not set the attribute of immutable class')

    def __delattr__(self, item):
        raise AttributeError("Can not delete the  attribute of immutable class")


if __name__ == '__main__':
    dog = Doggy('foo', 'boo', 18)
    print(dog.name)
    print(dog.age)
    print(dog.say)

    try:
        del dog.name
    except AttributeError:
        print(dog.name)

    try:
        dog.name = 'boris'
    except AttributeError:
        print(dog.name)

    object.__setattr__(dog, 'name', 'Changed')
    print(dog.name)
