from random import randint as ri

def partition(array, low, high):
    pivot = array[high]

    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:

            i = i + 1

            (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[high]) = (array[high], array[i + 1])

    return i + 1


def quickSort(array: list[int | float], low: int | float, high: int | float) -> None:
    ''' quicksort
    :param array: list[int | float]
    :param low: int | float
    :param high: int | float
    :return: None
    '''
    if low < high:

        pi = partition(array, low, high)

        quickSort(array, low, pi - 1)

        quickSort(array, pi + 1, high)


if __name__ == '__main__':

    data = [ri(0, 150) for _ in range(150)]
    print("Unsorted Array")
    print(data)

    size = len(data)

    quickSort(data, 0, size - 1)

    print('Sorted Array in Ascending Order:')
    print(data)