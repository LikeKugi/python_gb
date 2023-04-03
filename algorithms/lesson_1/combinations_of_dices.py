from itertools import combinations_with_replacement
from functools import wraps
import time

count_dices = int(input())
count_faces = int(input())

print(*combinations_with_replacement(range(1, count_faces + 1), count_dices))


def timer(func):
    @wraps(func)
    def inner(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f'time: {end - start}')
    return inner


@timer
def counter(count_faces):
    for i in range(1, count_faces + 1):
        for j in range(1, count_faces + 1):
            for k in range(1, count_faces + 1):
                for l in range(1, count_faces + 1):
                    for ii in range(1, count_faces + 1):
                        for ji in range(1, count_faces + 1):
                            for ki in range(1, count_faces + 1):
                                for li in range(1, count_faces + 1):
                                    for ij in range(1, count_faces + 1):
                                        for jj in range(1, count_faces + 1):
                                            for kj in range(1, count_faces + 1):
                                                for lj in range(1, count_faces + 1):
                                                    print(i, j, k, l)


counter(count_faces)
