import tkinter as tk

# Cria nossa janela
root = tk.Tk()

# Dá um título à janela
root.title('Hello World')

# Instância de label, associado à janela root
lbl = tk.Label(root, text='Hello World')
# Gerenciador de layout place, definindo a distância x e y do label dentro da janela.
lbl.place(x=50,y=50)

# Altera o tamanho da nossa janela.
# Lembrando que podemos usar root.geometry('NxM+x+y'), sendo x e y as distâncias do topo
# superior esquerdo para baixo e para a direita da tela.
root.geometry('250x250')

# Loop para manter nossa janela aberta.
root.mainloop()