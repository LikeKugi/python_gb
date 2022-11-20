# Дана квадратная матрица, заполненная случайными числами. Определите,
# сумма элементов каких строк превосходит сумму главной диагонали матрицы.
import numpy as np


def get_int_number(*args: str) -> int:
    return int(input(*args))


def create_random_matrix(n: int, max_val: int) -> np.array:
    return np.random.randint(max_val, size=(n, n))


def find_sum_main_diagonal(matrix: np.array) -> int:
    return np.trace(matrix)


def find_sum_rows(matrix: np.array, target: int) -> list:
    sum_of_rows = np.sum(matrix, axis=1)
    return list(filter(lambda x: x[1] > target, enumerate(sum_of_rows)))


def main():
    n = get_int_number('how many rows? ')
    max_val = get_int_number('max value in matrix? ')

    matrix = create_random_matrix(n, max_val)
    print(matrix)
    trace = find_sum_main_diagonal(matrix)

    target_rows = find_sum_rows(matrix, trace)
    for index, sum_row in target_rows:
        print(f'{index} row sum = {sum_row} > {trace}')


if __name__ == '__main__':
    main()
