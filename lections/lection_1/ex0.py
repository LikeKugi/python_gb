var = None
print(type(var))
a = 123
b = 1.23
print(a)
print(b)
var = 32
print(var, type(var))
s = 'hello world'
print(s)
print('{} - {} - {}'.format(a, b, s))
print('{1} - {2} - {0}'.format(a, b, s))
print(f'{a} - {b} - {s}')

a = 1 > 4
print(a)

a = 'qwe'
b = 'qwe'
print(a == b)

a = 3
b = 4
if a > b:
    print(a)
else:
    print(b)
