import tkinter as tk


root = tk.Tk()
root.title('Menu Test')

# Instancia o menu na janela root
menubar = tk.Menu(root)
# Adiciona os botões do menu
menubar.add_command(label='T1', command=lambda: print('ok'))
menubar.add_command(label='T2', command=root.quit)

# Inicia o menu
root.config(menu=menubar)

root.mainloop()