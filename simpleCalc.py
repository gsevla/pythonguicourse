import tkinter as tk
from tkinter import ttk


def calculate(e1, e2, op, lb):
    if(e1.isnumeric() and e2.isnumeric()):
        e1 = int(e1)
        e2 = int(e2)
        if(op == '+'):
            lb['text'] = e1+e2
        elif(op == '-'):
            lb['text'] = e1-e2
        elif(op == '*'):
            lb['text'] = e1*e2
        elif(op == '/'):
            lb['text'] = e1/e2
        else:
            lb['text'] = 'Something is wrong!'
    else:
        lb['text'] = 'A or B are not numeric!'

root = tk.Tk()
root.title('Simple Calc')

sCalc = tk.Frame(root)
sCalc.pack(fill='both', expand=True)

lbl1 = tk.Label(sCalc, text='A')
lbl1.grid(row=0,column=0)
lbl2 = tk.Label(sCalc, text='B')
lbl2.grid(row=0,column=1)

e1 = ttk.Entry(sCalc)
e1.grid(row=1,column=0)
e2 = ttk.Entry(sCalc)
e2.grid(row=1,column=1)

btn1 = tk.Button(sCalc, text='+', width=4, font=',14', command=lambda: calculate(e1.get(),e2.get(),'+',lbl3))
btn1.grid(row=0,column=2)
btn1 = tk.Button(sCalc, text='-', width=4, font=',14', command=lambda: calculate(e1.get(),e2.get(),'-',lbl3))
btn1.grid(row=1,column=2)
btn1 = tk.Button(sCalc, text='*', width=4, font=',14', command=lambda: calculate(e1.get(),e2.get(),'*',lbl3))
btn1.grid(row=2,column=2)
btn1 = tk.Button(sCalc, text='/', width=4, font=',14', command=lambda: calculate(e1.get(),e2.get(),'/',lbl3))
btn1.grid(row=3,column=2)

lbl3 = tk.Label(sCalc, text='0', fg='lightcoral')
lbl3.grid(row=2, rowspan=2, column=0, columnspan=2)

root.mainloop()