def f(x):
    return x ** 2


print(f(2))


def calc1(x):
    return x + 10


print(calc1(10))


def sm(x, y):
    return x + y


def product(x, y):
    return x * y


def calc(op, a, b):
    print(op(a, b))


calc(product, 4, 5)


with open('numbers.txt') as inf:
    numbers = list(map(lambda x: (x,x**2), filter(lambda x: x % 2 == 0, map(int, inf.readline().split()))))
print(numbers)