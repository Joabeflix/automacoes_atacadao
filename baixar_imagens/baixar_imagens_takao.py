import requests
import pandas as pd
import time
import os

def baixar_imagem(url, local_salvar):
    try:
        time.sleep(0.2)
        print(f'Tentando baixar no link: {url}')
        resposta = requests.get(url)
        resposta.raise_for_status()
        with open(local_salvar, 'wb') as f:
            f.write(resposta.content)
        print(f"Imagem baixada e salva em {local_salvar}")
        return True
    except Exception as e:
        print(f"Falha ao baixar a imagem de {url}: {e}")
        return False
 
planilha = pd.read_excel(r'takao.xlsx')
lista_codigos = planilha['codigo']

os.chdir('imagens')
lista_erros = []
links = [
    "https://cdn.takao.com.br/images-mult-prod/1000/codigo_produto/0.jpg",
    "https://cdn.takao.com.br/images-mult-prod/750/codigo_produto/0.jpg",
    "https://takao.blob.core.windows.net/images-mult-prod/1000/codigo_produto/0.jpg",
    "https://takao.blob.core.windows.net/images-mult-prod/1000/codigo_produto/0.jpg"
]

for codigo in lista_codigos:

    local_salvar = rf'{codigo.replace(" ", "")}.jpg'

    url = f'{links[0].replace("codigo_produto", codigo)}'
    if baixar_imagem(url, local_salvar=local_salvar):
        continue

    url = f'{links[1].replace("codigo_produto", codigo)}'
    if baixar_imagem(url, local_salvar=local_salvar):
        continue

    url = f'{links[2].replace("codigo_produto", codigo)}'
    if baixar_imagem(url, local_salvar=local_salvar):
        continue

    url = f'{links[3].replace("codigo_produto", codigo)}'
    if baixar_imagem(url, local_salvar=local_salvar):
        continue

    lista_erros.append(codigo)
