# Если необходимо, исправьте данный код(задание 2)

def create_array(d=0):
    try:
        arr = [i / d for i in range(8)]
        return arr
    except ZeroDivisionError as e:
        print(e)


def main():
    arr = create_array()
    print(arr)


if __name__ == '__main__':
    main()
