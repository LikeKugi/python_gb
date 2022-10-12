from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'], )
a = Point(3, 4)
print(a)
print(a.x)
print(a.y)