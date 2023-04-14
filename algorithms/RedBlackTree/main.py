from RedBlackTree import RedBlackTree


def main():
    rbt = RedBlackTree()
    for i in range(50):
        rbt.insert(i)
    rbt.print()


if __name__ == '__main__':
    main()
