from tkinter import *


win = Tk()
win.title('my app')
win.geometry('700x700')


def hendleClickButoon():
    print('helo')
question_1 = Entry(win)
question_1
Entry(win).place(width=150, heigh=50, x=150, y=150)
Entry(win).place(width=150, heigh=50, x=150, y=200)
Entry(win).place(width=150, heigh=50, x=150, y=250)
Entry(win).place(width=150, heigh=50, x=150, y=300)
Entry(win).place(width=150, heigh=50, x=150, y=350)

Button(text='click me', command=hendleClickButoon).place(width=150, heigh=50, x=150, y=50)

win.mainloop()