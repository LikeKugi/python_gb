import math


def binary_search(query: int | float, arr: list[int | float]) -> int:
    """
    binary search
    :param query: int | float
    :param arr: list[int | float]
    :return: int - index of the query or -1 in query not in arr1
    """

    end = len(arr) - 1
    start = 0
    i = math.floor((end) / 2)
    while start <= i <= end:
        if arr[i] == query:
            return i
        if arr[i] > query:
            end = i - 1
        else:
            start = i + 1
        i = math.floor((end + start) / 2)
    return -1


if __name__ == '__main__':
    arr = [i for i in range(100)]
    print(binary_search(15, arr))
