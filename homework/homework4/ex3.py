# Выведите число π с заданной точностью. Точность вводится пользователем в виде натурального числа.
from math import pi as PI
from random import uniform as ru


def get_int_number(*args): return int(input(*args))


def print_pi(pi, dg):
    print(round(pi, dg))


def finding_pi():
    n = 10 ** 7  # количество испытаний
    k = 0  # количество точек внутри фигуры
    s0 = 4  # площадь квадрата в котором фигура
    print('waiting for counting PI')
    for _ in range(n):
        x = ru(-1, 1)
        y = ru(-1, 1)

        if x ** 2 + y ** 2 <= 1:
            k += 1
    print('DONE')
    return (k / n) * s0


def main():
    n = get_int_number('how many digits in PI: ')
    var = get_int_number('1 to math.PI, else to Monte Carlo finding PI: ')
    if var == 1:
        print_pi(PI, n)
    else:
        print_pi(finding_pi(), n)


if __name__ == '__main__':
    main()
