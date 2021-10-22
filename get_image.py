import cv2
from tkinter import *
from PIL import Image, ImageTk


def show_camera():
    global img_read
    vid = cv2.VideoCapture(0)
    # while(True):
    ret, frame = vid.read()
    # Display the resulting frame
    # cv2.imshow('frame', frame)
    cv2.imwrite('me.png', frame)
    # cv2.waitKey(0)
    # # Destroy all the windows
    # cv2.destroyAllWindows()
    img_read = ImageTk.PhotoImage(Image.open('me.png').resize((600, 600), Image.ANTIALIAS))
    Label(win, image=img_read).place(width=600, heigh=600, x=50, y=250)


win = Tk()
win.title('my_app')
win.geometry('700x900+1000+100')

Button(win, text='get image', command=show_camera).place(width=100, heigh=30, x = 50, y = 50)


win.mainloop()