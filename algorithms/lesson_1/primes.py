import math


def is_prime(n):
    if n < 4:
        return n > 1
    if not (n % 2) or not (n % 3):
        return False
    for i in range(5, math.ceil(math.sqrt(n)), 6):
        if not (n % i) or not (n % (i + 2)):
            return False
    return True


for i in range(100):
    print(i, is_prime(i))
