from Node import LinkedList


def main():
    linked = LinkedList()

    for i in range(50):
        linked.append(i)

    print(linked)

    print(linked.includes(15))
    print(linked.includes(75))

    print(linked.tail)


def for_sort():
    linked = LinkedList()
    linked.append(5)
    linked.append(2)
    linked.append(6)
    linked.append(2)
    linked.append(9)
    linked.append(3)
    print(linked)
    linked.sort()
    print(linked)
    linked.reverse()
    print(linked)


if __name__ == '__main__':
    main()
    for_sort()
