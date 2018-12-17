import tkinter as tk

root = tk.Tk()
root.title('Hello World')
lbl = tk.Label(root, text='Hello World')
lbl.place(x=50,y=50)
root.geometry('250x250')
root.mainloop()