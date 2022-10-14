# Считайте строковые данные из файла.
# Создайте словарь, содержащий все символы в
# файле.

def read_file():
    lines = list()
    with open('file.txt', 'r', encoding='utf-8') as inf:
        lines.extend(inf.readlines())
    return lines


def create_dict(lines):
    chars = {}
    for line in lines:
        for char in line:
            chars[char] = chars.setdefault(char, 0) + 1
    print(chars)


def main():
    lines_of_file = read_file()
    create_dict(lines_of_file)


if __name__ == '__main__':
    main()
