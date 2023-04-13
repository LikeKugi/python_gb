from hash_table import HashTable


def add(ht: HashTable):
    for i in range(20):
        ht.insert(i)
        print(ht)


def find(ht: HashTable, query: str | int):
    return ht.find(query)


if __name__ == '__main__':
    table = HashTable()
    table.insert('value')
    print(table)
    table.insert('here')
    print(table)
    add(table)

    print(find(table, 13))

    print(table)
    table.delete(13)
    print(table)
