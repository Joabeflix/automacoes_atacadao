import requests
import os
import pandas as pd

def baixar_imagem(url, local_salvar):
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
        with open(local_salvar, 'wb') as f:
            f.write(resposta.content)
        print(f"Imagem baixada e salva em {local_salvar}")
        return True
    except Exception as e:
        print(f"Falha ao baixar a imagem de {url}: {e}")
        return False

planilha = pd.read_excel(r'baixar_imagens\Links.xlsx')
lista_links = planilha['link']
lista_nomes = planilha['nome']

lista_erros = []

for l, n in zip(lista_links, lista_nomes):
    local_salvar = f'baixar_imagens/imagens/{n}.jpg'
    if baixar_imagem(url=l, local_salvar=local_salvar):
        continue
    lista_erros.append(n)

if lista_erros:
    print('Erros:')
    for err in lista_erros:
        print(f'---> {err}')
