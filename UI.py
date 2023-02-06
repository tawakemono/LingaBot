from tkinter import *
from tkinter import ttk


def Getinfo(a):
    User = a

def close_window():
    root.destroy()

root = Tk()
root.title('LingaBot')
root.resizable(False, False)
frame1 = ttk.Frame(root, padding=(32))
frame1.grid()

label1 = ttk.Label(frame1, text='Username', padding=(5, 2))
label1.grid(row=0, column=0, sticky=E)

label2 = ttk.Label(frame1, text='Password', padding=(5, 2))
label2.grid(row=1, column=0, sticky=E)

label2 = ttk.Label(frame1, text='StartNum', padding=(5, 2))
label2.grid(row=2, column=0, sticky=E)

label2 = ttk.Label(frame1, text='EndNum', padding=(5, 2))
label2.grid(row=3, column=0, sticky=E)

# Username Entry
username = StringVar()
username_entry = ttk.Entry(
    frame1,
    textvariable=username,
    width=20)
username_entry.grid(row=0, column=1)

# Password Entry
password = StringVar()
password_entry = ttk.Entry(
    frame1,
    textvariable=password,
    width=20,
    show='*')
password_entry.grid(row=1, column=1)

#StartNum Entry
StartNum = StringVar()
StartNum_entry = ttk.Entry(
    frame1,
    textvariable=StartNum,
    width=20)
StartNum_entry.grid(row=2, column=1)

#EndNum Entry
EndNum = StringVar()
EndNum_entry = ttk.Entry(
    frame1,
    textvariable=EndNum,
    width=20)
EndNum_entry.grid(row=3, column=1)

frame2 = ttk.Frame(frame1, padding=(0, 5))
frame2.grid(row=4, column=1, sticky=W)

button1 = ttk.Button(
    frame2, text='OK',
    command=lambda:[Getinfo(username.get()),close_window()])
button1.pack(side=LEFT)

button2 = ttk.Button(frame2, text='Cancel', command=quit)
button2.pack(side=LEFT)

root.mainloop()



print(str(username.get()))
print(str(password.get()))
print(str(StartNum.get()))
print(str(EndNum.get()))




