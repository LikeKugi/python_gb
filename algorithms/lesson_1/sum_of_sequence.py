m = int(input())


def sum_sequence(n: int = 0) -> int | None:
    if (type(n) != int) or (n < 1): return None
    return sum(range(1, n + 1))


print(sum_sequence(m))
