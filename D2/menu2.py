import tkinter as tk


root = tk.Tk()
root.title('Menu Test')

# Instancia o menu na janela root
menubar = tk.Menu(root)

# Instancia o submenu file sem tearoff
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label='T1', command=lambda: print('ok'))
# Como o nome diz, é um separador
filemenu.add_separator()
filemenu.add_command(label='T2', command=root.quit)
# Adiciona o botão file como cascata
menubar.add_cascade(label='File', menu=filemenu)

# Instancia o submenu about sem tearoff
aboutmenu = tk.Menu(menubar, tearoff=0)
aboutmenu.add_command(label='T3', command=lambda: print('ok'))
aboutmenu.add_command(label='T4', command=root.quit)
# Adiciona o botão about como cascata
menubar.add_cascade(label='About', menu=aboutmenu)

# Inicia o menu
root.config(menu=menubar)

root.mainloop()