import pandas as pd
import os

planilha = pd.read_excel('plan.xlsx')
coluna_codigos = planilha['mpn']

coluna_nova = []

os.chdir(r'C:\Users\joab.alves\Desktop\img-cad-api')
fotos = os.listdir()


for codigo in coluna_codigos:
    codigo = f'{codigo}.jpg'
    if codigo in fotos:
        coluna_nova.append('OK')
        continue
    coluna_nova.append('Não')

planilha['Foto'] = coluna_nova
salvar = planilha.to_excel('verif.xlsx', index=False)

