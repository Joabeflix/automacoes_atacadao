import tkinter as tk

def printar(vezes_click=1):
    print(f'Clicou no botao {vezes_click} vezes!')
    vezes_click+=1



tela = tk.Tk()
tela.geometry('500x370')
tela.title('meu teste')

entrada = tk.Entry(tela, width=40)
entrada.pack()

botao = tk.Button(tela, width=16, text='Clique', command=lambda: printar())
botao.pack()



tela.mainloop()