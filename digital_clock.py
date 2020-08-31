from tkinter import *
import time
import datetime

root = Tk()
root.title('Digital Clock')
root.geometry('500x250+0+0')
root.config(bg = '#081923')

def clock():
    h = str(time.strftime("%H"))
    m = str(time.strftime("%M"))
    s = str(time.strftime("%S"))
    time1 = datetime.datetime.now()
    time1 = time1.strftime("%d-%b-%y")

    if int(h) == 12 and int(m) == 0:
        lbl_ap.config(text='Noon', font=('Arial', 16, 'bold'))

    if int(h) >= 12 and int(m) > 0:
        lbl_ap.config(text='PM')

    if int(h) > 12:
        h = str(int(h) - 12)

    lbl_hr.config(text = h)
    lbl_min.config(text = m)
    lbl_sec.config(text = s)
    lbl_time.config(text = time1)

    lbl_hr.after(200, clock)

# For Hour
lbl_hr = Label(root, text = '12', font = ('Arial', 23, 'bold'), bg = 'Red', fg = 'White')
lbl_hr.place(x=82, y = 65, width = 60, height = 60)

lbl_hr2 = Label(root, text = 'Hour', font = ('Arial', 13, 'bold'), bg = 'Red', fg = 'White')
lbl_hr2.place(x=82, y = 135, width = 60, height = 20)

# For Min
lbl_min = Label(root, text = '12', font = ('Arial', 23, 'bold'), bg = 'Blue', fg = 'White')
lbl_min.place(x=170, y = 65, width = 60, height = 60)

lbl_min2 = Label(root, text = 'Minute', font = ('Arial', 13, 'bold'), bg = 'Blue', fg = 'White')
lbl_min2.place(x=170, y = 135, width = 60, height = 20)

# For Sec
lbl_sec = Label(root, text = '12', font = ('Arial', 23, 'bold'), bg = 'Green', fg = 'White')
lbl_sec.place(x=258, y = 65, width = 60, height = 60)

lbl_sec2 = Label(root, text = 'Second', font = ('Arial', 13, 'bold'), bg = 'Green', fg = 'White')
lbl_sec2.place(x=258, y = 135, width = 60, height = 20)

# For AM, PM
lbl_ap = Label(root, text = 'AM', font = ('Arial', 20, 'bold'), bg = 'yellow', fg = 'black')
lbl_ap.place(x=346, y = 65, width = 60, height = 60)

lbl_ap2 = Label(root, text = 'Noon', font = ('Arial', 13, 'bold'), bg = 'yellow', fg = 'black')
lbl_ap2.place(x=346, y = 135, width = 60, height = 20)

lbl_time = Label(root, text = '', font = ('Arial', 20, 'bold'), bg = 'white', fg = 'black')
lbl_time.place(x=145, y = 170, width = 200, height = 60)

clock()

root.mainloop()