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

label1 = ttk.Label(frame1, text='Username', padding=(5, 2), foreground='#ff0000')
label1.grid(row=0, column=0, sticky=W)

label2 = ttk.Label(frame1, text='Password', padding=(5, 2), foreground='#ff0000')
label2.grid(row=1, column=0, sticky=W)

label3 = ttk.Label(frame1, text='StartNum', padding=(5, 2), foreground='#ff0000' )
label3.grid(row=2, column=0, sticky=W)

label4 = ttk.Label(frame1, text=' 1-25の場合は1, 126-150の場合は126', padding=(0, 0))
label4.grid(row=3, column=0, columnspan = 2, sticky=W)

label5 = ttk.Label(frame1, text='EndNum', padding=(5, 2), foreground='#ff0000')
label5.grid(row=4, column=0, sticky=W)

label6 = ttk.Label(frame1, text=' 976-1000を最後にするなら1000', padding=(0, 0))
label6.grid(row=5, column=0, columnspan = 2, sticky=W)

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
EndNum_entry.grid(row=4, column=1)

frame2 = ttk.Frame(frame1, padding=(0, 5))
frame2.grid(row=6, column=0, columnspan = 2, sticky=N)

button1 = ttk.Button(
    frame2, text='OK',
    command=lambda:[Getinfo(username.get()),close_window()])
button1.pack(side=LEFT)

button2 = ttk.Button(frame2, text='Cancel', command=quit)
button2.pack(side=LEFT)

root.mainloop()

loginid = str(username.get())
Loginpass = str(password.get())
Unitnum = int(StartNum.get())
Unitnum_end = int(EndNum.get())

print(str(username.get()))
print(str(password.get()))
print(str(StartNum.get()))
print(str(EndNum.get()))




