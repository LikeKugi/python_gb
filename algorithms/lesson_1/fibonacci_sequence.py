from functools import lru_cache


def iter_fib(n):
    a, b = 0, 1
    for i in range(n + 1):
        a, b = a + b, a
    return a


@lru_cache()
def req_fib(n):
    if n in {0, 1}:
        return 1
    return req_fib(n - 1) + req_fib(n - 2)


for i in range(700):
    print(f'{i}: {iter_fib(i)}')
    print(f'{i}: {req_fib(i)}')
    print()
