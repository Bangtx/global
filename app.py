from tkinter import *
from tkinter.messagebox import *
import math
from readAns import Ans

win = Tk()
win.title('my app')
win.geometry('700x500+500+100')

user = ''
passw = ''
user_base = 'admin'
passw_base = 'admin'


def process():
    a = int(a_entry.get())
    b = int(b_entry.get())
    c = int(c_entry.get())
    denta = b*b - 4*a*c
    if denta < 0:
        showinfo('info', 'phương trình vô nghiệm')
    if denta == 0:
        x = -b/(2*a)
        showinfo('info', f'phương trình có nghiệm kép x = {x}')
    if denta > 0:
        x_1 = (-b + math.sqrt(denta))/(2*a)
        x_2 = (-b - math.sqrt(denta))/(2*a)
        showinfo('info', f'phương trình có 2 nghiệm phân biệt x1 = {x_1}, x2={x_2}')


def mainScreen():
    global a_entry, b_entry, c_entry
    Label(win).place(width=700, heigh=500, x=0, y=0)
    Label(win, text='nhap a').place(width=100, heigh=30, x=0, y=50)
    a_entry = Entry(win)
    a_entry.place(width=100, heigh=30, x=100, y=50)
    Label(win, text='nhap b').place(width=100, heigh=30, x=200, y=50)
    b_entry = Entry(win)
    b_entry.place(width=100, heigh=30, x=300, y=50)
    Label(win, text='nhap c').place(width=100, heigh=30, x=400, y=50)
    c_entry = Entry(win)
    c_entry.place(width=100, heigh=30, x=500, y=50)
    Button(win, text='process', command=process).place(width=100, heigh=30, x=300, y=150)



def handleClickButtonLogin():
    user = user_entry.get()
    passw = password_entry.get()
    if user == user_base and passw == passw_base:
        mainScreen()
    else:
        showerror('error', 'Sai Tk Hoặc Mk')


Label(win, text='welcome', font='times 20', fg='red').place(
    width=200, heigh=50, x=250, y=50
)
Label(win, text='user', font='times 15').place(
    width=200, heigh=50, x=250, y=150
)
user_entry = Entry(win)
user_entry.insert(0, 'admin')
user_entry.place(width=100, heigh=30, x=300, y=200)
Label(win, text='pass', font='times 15').place(
    width=200, heigh=50, x=250, y=250
)
password_entry = Entry(win, show='*')
password_entry.insert(0, 'admin')
password_entry.place(width=100, heigh=30, x=300, y=300)
Button(win, text='login', command=handleClickButtonLogin).place(width=100, heigh=30, x=300, y=350)

win.mainloop()
