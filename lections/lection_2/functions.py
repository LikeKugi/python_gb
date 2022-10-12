def new_string(symbol, count):
    return symbol * count


print(new_string('!',5))


def concatenatio(*params):
    res: str = ""
    for item in params:
        res += str(item)
    return res


print(concatenatio('1','4','hello','world'))