import tkinter as tk
from tkinter import ttk


# Informações definidas para teste
LOGIN = 'pet'
PASSWORD = 'computacao'


# Função para verificação do usuário.
# Verifica se o login e o password estão conforme foram definidos e
# caso verdade, será aberta uma janela Toplevel parabenizando o usuário.
# Caso contrário, um label aparece avisando que algo está errado.
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


# Janela raiz
root = tk.Tk()
root.title('Login Screen')

# Instancia um Frame(container) dentro da janela principal
lScreen = tk.Frame(root)
lScreen.pack()

# Instâncias dos labels, entries e buttons, utilizando grid para melhor posicioná-los
# Lembrando que não podemos utilizar dois gerenciadores de layout diferentes em um mesmo frame
# Logo, podemos perceber a seguinte hierarquia: root > Frame
# Como o Frame foi posicionado com pack, dentro de root, em root apenas se usa pack
# Já dentro do Frame, como usamos o grid abaixo, apenas podemos usar grid.
lb1 = tk.Label(lScreen, text='Login')
lb2 = tk.Label(lScreen, text='Password')
lb1.grid(row=0, column=0)
lb2.grid(row=1, column=0)

e1 = ttk.Entry(lScreen)
# O argumento show é usado para substituir os caracteres digitados pelo seu valor
e2 = ttk.Entry(lScreen, show='*')
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

btn1 = tk.Button(lScreen, text='  OK  ', command=lambda: verify(lScreen, e1.get(), e2.get()))
btn1.grid(row=2, column=0, columnspan=2)

# Loop
root.mainloop()