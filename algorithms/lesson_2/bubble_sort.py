from random import randint as ri


def bubble_sort(arr: list[int | float]) -> list[int | float]:
    ''' Bubble sort
    :param arr: list[int|float]
    :return: sorted arr
    '''
    flag = True
    k = 0
    while flag:
        flag = False
        for i in range(len(arr) - 1 - k):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                flag = True
        else:
            if not flag:
                return arr


if __name__ == '__main__':
    arr = [ri(0, 150) for _ in range(100)]
    print(arr)
    print(bubble_sort(arr))
