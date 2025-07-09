import pandas as pd
import os
from tkinter import filedialog

planilha = pd.read_excel('plan.xlsx')
coluna_codigos = planilha['mpn']

coluna_nova = []

print('Selecione a pasta das imagens')
os.chdir(filedialog.askdirectory())

fotos = os.listdir()

lista_nao = []

for codigo in coluna_codigos:
    codigo = f'{codigo}.jpg'
    if codigo in fotos:
        coluna_nova.append('OK')
        continue
    coluna_nova.append('Não')
    lista_nao.append(codigo)

planilha['Foto'] = coluna_nova
salvar = planilha.to_excel('verif.xlsx', index=False)
print('Planilha salva com os dados.')

if lista_nao:
    print('\nLista de produtos que não está com imagens:')
    for x in lista_nao:
        print(x)
