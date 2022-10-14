# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

def get_number(*texts): return int(input(*texts))


def convert_to_binary(n):
    binary = ''
    while n != 0:
        binary = str(n % 2) + binary
        n //= 2
    return binary


def main():
    number = get_number('input number to convert: ')
    converted = convert_to_binary(number)
    print(f'{number} in binary = {converted}')

if __name__ == '__main__':
    main()