from tkinter import filedialog
import os

caminho_txt_ = rf'{os.getcwd()}\imagens_verificar.txt'

print('Selecione a pasta das imagens')

os.chdir(filedialog.askdirectory())

fotos = os.listdir()
lista_nao = []

with open(caminho_txt_, 'r') as file:
    for codigo in file:
        _codigo = codigo.strip()
        _codigo = f'{_codigo}.jpg'

        if _codigo not in fotos:
            lista_nao.append(codigo)

if lista_nao:
    print('\nLista de produtos que não está com imagens:')
    for codigo in lista_nao:
        print(codigo)

if not lista_nao:
    print('Todas as imagens está OK')
