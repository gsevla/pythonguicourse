import tkinter as tk
from tkinter import ttk


LOGIN = 'pet'
PASSWORD = 'computacao'


def verify(window, lg, ps):
    if(lg == LOGIN and ps == PASSWORD):
        popup = tk.Toplevel()
        popup.wm_title('!')
        #popup.tkraise(root)
        plbl = tk.Label(popup, text='Congratulations, you did it!')
        plbl.pack()
        pbtn = tk.Button(popup, text='  OK  ', command=popup.destroy)
        pbtn.pack()
    else:
        lbtest = tk.Label(window, text='Something is wrong!', fg='red')
        lbtest.grid(row=3, column=0, columnspan=2)


root = tk.Tk()
root.title('Login Screen')

lScreen = tk.Frame(root)
lScreen.pack()

lb1 = tk.Label(lScreen, text='Login')
lb2 = tk.Label(lScreen, text='Password')
lb1.grid(row=0, column=0)
lb2.grid(row=1, column=0)

e1 = ttk.Entry(lScreen)
e2 = ttk.Entry(lScreen)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

btn1 = tk.Button(lScreen, text='  OK  ', command=lambda: verify(lScreen, e1.get(), e2.get()))
btn1.grid(row=2, column=0, columnspan=2)


lScreen.mainloop()