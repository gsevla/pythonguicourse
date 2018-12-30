import tkinter as tk
from tkinter import ttk


# Função usada nos botões
# ela apenas verifica se as entradas são numéricas e, caso isso seja verdade,
# transforma as entradas em inteiros e realiza as operações.
# Repare que usamos o conceito de dicionário, modificando o valor da propriedade text do label.
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

# Janela raiz
root = tk.Tk()
root.title('Simple Calc')

# Instancia um Frame(container) dentro da janela principal
sCalc = tk.Frame(root)
# Pack com fill='both' e expand=True usados para preenchimento e expansão de widgets
sCalc.pack(fill='both', expand=True)

# Instâncias dos labels, entries e buttons, utilizando grid para melhor posicioná-los
# Lembrando que não podemos utilizar dois gerenciadores de layout diferentes em um mesmo frame
# Logo, podemos perceber a seguinte hierarquia: root > Frame
# Como o Frame foi posicionado com pack, dentro de root, em root apenas se usa pack
# Já dentro do Frame, como usamos o grid abaixo, apenas podemos usar grid.
lbl1 = tk.Label(sCalc, text='A')
lbl1.grid(row=0,column=0)
lbl2 = tk.Label(sCalc, text='B')
lbl2.grid(row=0,column=1)

e1 = ttk.Entry(sCalc)
e1.grid(row=1,column=0)
e2 = ttk.Entry(sCalc)
e2.grid(row=1,column=1)

# Para o command, apenas passamos a referência da função, ou seja, não usamos func(), mas sim func
# Para que possamos passar funções completas, usamos a expressão lambda, sem passarmos nome, 
# a fim de que ela atue como uma função anônima, para que possamos chamar uma outra função
# dentro dela e, nessa, sim, podemos passar nossos argumentos.
btn1 = tk.Button(sCalc, text='+', width=4, font=',14', command=lambda: calculate(e1.get(),e2.get(),'+',lbl3))
btn1.grid(row=0,column=2)
btn1 = tk.Button(sCalc, text='-', width=4, font=',14', command=lambda: calculate(e1.get(),e2.get(),'-',lbl3))
btn1.grid(row=1,column=2)
btn1 = tk.Button(sCalc, text='*', width=4, font=',14', command=lambda: calculate(e1.get(),e2.get(),'*',lbl3))
btn1.grid(row=2,column=2)
btn1 = tk.Button(sCalc, text='/', width=4, font=',14', command=lambda: calculate(e1.get(),e2.get(),'/',lbl3))
btn1.grid(row=3,column=2)

# rowspan e columnspan servem para centralizar widgets entre linhas e colunas respectivamente
lbl3 = tk.Label(sCalc, text='0', fg='lightcoral')
lbl3.grid(row=2, rowspan=2, column=0, columnspan=2)

# Loop
root.mainloop()