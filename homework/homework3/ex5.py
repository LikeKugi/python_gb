# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
import numpy as np
import cowsay  # самый нужный модуль в питоне, настало твоё время)


def get_int_number(*texts): return int(input(*texts))


def create_array_fibonacci(n):
    f1, f2 = 1, 1
    numbers = np.zeros(n, dtype=np.int_)
    for i in range(n):
        numbers[i] = f1
        f1, f2 = f2, f1 + f2
    return numbers


def create_nega_fibonacci(fibonacci: np.array):
    neg_fib = np.array([(-1, 1)[i % 2 == 0] * fibonacci[i] for i in range(len(fibonacci))])
    return neg_fib


def create_whole_fibonacci(fib:np.array, neg_fib:np.array):
    whole = list()
    whole.extend(list(reversed(neg_fib)))
    whole.append(0)
    whole.extend(list(fib))
    return whole

def main():
    cowsay.cow('the fibonacci sequence ')
    number = get_int_number('enter value of fibonacci: ')
    fibonacci_sequence = create_array_fibonacci(number)
    negative_fibonacci = create_nega_fibonacci(fibonacci_sequence)
    whole_sequence = create_whole_fibonacci(fibonacci_sequence,negative_fibonacci)
    print(f'the whole sequence:\n ',*whole_sequence)


if __name__ == '__main__':
    main()
