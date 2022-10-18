# Создайте игру в кости. Игрок играет против бота.
# Каждый поочерёдно кидает по два кубика. Реализуйте игре интерфейс с помощью библиотеки tkinter.
from tkinter import *
from random import randint as ri


def move():
    return ri(1, 6), ri(1, 6)


def clicked():
    global sum_gamer
    global sum_bot
    cubes = move()
    sum_gamer += sum(cubes)
    lbl.configure(text=str(cubes))
    lbl_sum.configure(text=str(sum_gamer))
    cubes = move()
    sum_bot += sum(cubes)
    bot_lbl.configure(text=str(cubes))
    bot_lbl_sum.configure(text=str(sum_bot))
window = Tk()
window.title("Кубики")
window.geometry('700x500')
ttl = Label(window, text="Текущие броски", font=("Arial Bold", 20))
ttl.grid(column=0, row=0)
ttl_sum = Label(window, text="Сумма", font=("Arial Bold", 20))
ttl_sum.grid(column=2, row=0)
lbl = Label(window, text="Твои кости", font=("Arial Bold", 50))
lbl.grid(column=0, row=1)
lbl_sum = Label(window, text="yours_sum", font=("Arial Bold", 50))
lbl_sum.grid(column=1, row=1)
bot_lbl = Label(window, text="Кости бота", font=("Arial Bold", 50))
bot_lbl.grid(column=0, row=2)
bot_lbl_sum = Label(window, text="yours_sum", font=("Arial Bold", 50))
bot_lbl_sum.grid(column=1, row=2)
sum_gamer = 0
sum_bot = 0
btn = Button(window, text="Бросок", command=clicked)
#lbl.configure(text=str(move()))
btn.grid(column=0, row=3)
window.mainloop()

