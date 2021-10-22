from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from readAns import *
from processImage import process_image
import time
from PIL import Image, ImageTk
win = Tk()
win.title('my_app')
win.geometry('700x900+500+50')
list_ans = dict()
mssv = ''
md = ''
diem = ''
path_file = ''


def openDialog():
    global list_ans, path_file
    path_file_entry.delete(0, END)
    path_file = filedialog.askopenfilename(initialdir="C:/", title="select file",
                                          filetypes=(("excel files", "*.xlsx"), ("all files", "*.*")))
    path_file_entry.insert(0, path_file)
    ans = Ans(path_file)
    list_ans = ans.readFile()


def openDialogChooseStudents():
    global list_ans, path_file_student
    path_file_student_entry.delete(0, END)
    path_file_student = filedialog.askopenfilename(initialdir="C:/", title="select file",
                                          filetypes=(("excel files", "*.xlsx"), ("all files", "*.*")))
    path_file_student_entry.insert(0, path_file_student)



def click_process_image():
    global img_read, path_file
    openDialog()
    openDialogChooseStudents()
    if path_file != '':
        mssv, md, diem = process_image()
        time.sleep(0.01)
        img_read = ImageTk.PhotoImage(Image.open('process.png').resize((600,600), Image.ANTIALIAS))
        Label(win, image=img_read).place(width=600, heigh=600, x=50, y=250)
        Label(win, text=mssv, font='times 15', bg='white').place(width=100, heigh=50, x=70, y=100)
        Label(win, text=md, font='times 15', bg='white').place(width=100, heigh=50, x=270, y=100)
        Label(win, text=diem, font='times 15', bg='white').place(width=100, heigh=50, x=420, y=100)
        ex = Ans(path_file_student)
        ex.write_data(mssv, diem)
    else:
        messagebox.showerror('error', 'vui long chon file')


Label(win, text='chọn file đáp án').place(width=150, heigh=50, x=20, y=0)
path_file_entry = Entry(win)
path_file_entry.place(width=400, heigh=30, x=200, y=10)
Label(win, text='chọn file dsSv').place(width=150, heigh=50, x=20, y=50)
path_file_student_entry = Entry(win)
path_file_student_entry.place(width=400, heigh=30, x=200, y=60)
Label(win, text='mssv', font='times 15').place(width=50, heigh=50, x=20, y=100)
Label(win, text=mssv, font='times 15', bg='white').place(width=100, heigh=50, x=70, y=100)
Label(win, text='ma de', font='times 15').place(width=50, heigh=50, x=220, y=100)
Label(win, text=md, font='times 15', bg='white').place(width=100, heigh=50, x=270, y=100)
Label(win, text='diem', font='times 15').place(width=50, heigh=50, x=370, y=100)
Label(win, text=diem, font='times 15',bg='white').place(width=100, heigh=50, x=420, y=100)
Button(win, text='bat dau', font='times 15', command=click_process_image).place(width=100, heigh=50, x=550, y=100)

# img_folder = Image.open('folder.jpg')
# img_folder = img_folder.thumbnail((30, 30), Image.ANTIALIAS)
# img_folder = ImageTk.PhotoImage(img_folder)
Button(win, text='choose', command=openDialog).place(width=70, heigh=30, x=620, y=10)
Button(win, text='choose', command=openDialogChooseStudents).place(width=70, heigh=30, x=620, y=60)

win.mainloop()