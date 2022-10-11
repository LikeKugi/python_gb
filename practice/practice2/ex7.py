"""
Компьютер загадал пятизначное число.
Игрок должен его отгадать. Компьютер даёт подсказки на каждый ввод пользователя.
Компьютер выводит нули за каждую неотгаданную цифру числа, единицы - за каждую отгаданную цифру,
двойку - за каждую отгаданную цифру на правильной позиции.
Игра длится 15 ходов или пока игрок не отгадает число.
"""
from random import randint as ri


def create_number(): return ri(10_000, 100_000)


def quiz_game(number):
    move_count = 0
    arr_number = [int(el) for el in str(number)]
    score = 0
    while move_count < 16:
        move_count += 1
        checking = int(input('enter digit: '))
        pos = int(input('enter position: ')) - 1
        if checking not in arr_number:
            print(0)
        elif checking in arr_number:
            if arr_number[pos] == checking:
                print(2)
                score += 2
                arr_number[pos] = -1
            else:
                print(1)
                score += 1
                arr_number[arr_number.index(checking)] = -1
        if arr_number.count(-1) == 5:
            print('You won')
            print('number was', number)
            print('YOUR SCORE', score)
            break
    else:
        print('AHAHAHAH LOOSER')
        print('number was', number)
        print('YOUR SCORE', score)
        print('LOOSER')

def main():
    n = create_number()
    quiz_game(n)

if __name__ == '__main__':
    main()
