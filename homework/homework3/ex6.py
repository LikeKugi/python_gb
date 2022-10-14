# В файле находятся названия фруктов.
# Выведите все фрукты, названия которых начинаются на
# заданную букву

def get_first_letter(): return input()[0]

def find_fruits_from_file(letter:str):
    with open('fruits.txt','r',encoding='utf-8') as inf:
        fruits = [inf.readline().strip().replace('\n','') for _ in inf]
    print(fruits)
    for fruit in fruits:
        if fruit and fruit[0].lower() == letter.lower():
            print(fruit)

def main():
    char = get_first_letter()
    find_fruits_from_file(char)

if __name__ == '__main__':
    main()