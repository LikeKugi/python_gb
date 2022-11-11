#  Сколько дней до нового года

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from model import Date

current_date = Date()


def clicked():
    messagebox.showinfo('До нового года', str(current_date))


def fill_form(root, frm):
    ttk.Label(frm, text=current_date.get_today).grid(column=0, row=0)
    ttk.Button(frm, text="Calculate", command=clicked).grid(column=1, row=1)
    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=2)


def main():
    window = Tk()
    frm = ttk.Frame(window, padding=10)
    frm.grid(column=2, row=2)
    fill_form(window, frm)
    window.mainloop()


if __name__ == '__main__':
    main()
