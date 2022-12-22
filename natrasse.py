from tkinter import *
from tkinter import messagebox
import math

def calculate(*args):
        summa = int(a.get())
        summa2 = int(b.get())
        summa2 = (summa // 3) * (f + p + (c * 2) + (m * 2))
        b.set(str(summa2))
        Label(text="Сумма затрат протяжки трассы:").place(x=105, y=162.5)
        Entry(width=10, textvariable=b).place(x=290, y=162.5)

root = Tk()
root.title("Задача №6")
root.geometry('500x250')

f = 36000
p = 300000
c = 1200
m = 1200

a = StringVar()
b = StringVar()
b.set("0")

Label(root, text="Приложение для подсчета затрат на протяжку оптоволоконных трасс").place(x=60, y=15)

Label(root, text="Длина трассы (км):").place(x=5, y=83)
Entry(root, textvariable=a).place(x=115, y=85.5)

but = Button(root, command=calculate, padx=5, pady=1, font=5)
but.place(x=130, y=200)
but["text"] = "Посчитать затраты"

root.mainloop()