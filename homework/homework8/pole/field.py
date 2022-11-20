def create_array_answer(answer: dict) -> list[str]:
    length = max([i for row in answer.values() for i in row])
    new_field = ['_'] * (length + 1)
    return new_field


def put_char_in_field(char: str, field: list[str], ans: dict[str, list]):
    indexes = ans.get(char)
    for i in indexes:
        field[i] = char
