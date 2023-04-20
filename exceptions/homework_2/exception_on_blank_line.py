# Разработайте программу, которая выбросит Exception, когда пользователь вводит пустую строку.
# Пользователю должно показаться сообщение, что пустые строки вводить нельзя.
class BlankLineException(Exception):
    pass


def get_str():
    line = input('enter line: ')
    if not line:
        raise BlankLineException('Line can\'t be empty')
    return line


if __name__ == '__main__':
    try:
        string = get_str()
        print(string)
    except BlankLineException as e:
        print(e)