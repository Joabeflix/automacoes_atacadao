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
 
planilha = pd.read_excel(r'baixar_imagens\takao.xlsx')
lista_codigos = planilha['codigo']

os.chdir(rf'baixar_imagens\imagens')
lista_erros = []

for codigo in lista_codigos:

    links = [
        f"https://cdn.takao.com.br/images-mult-prod/1000/{codigo}/1.jpg",
        f"https://cdn.takao.com.br/images-mult-prod/1000/{codigo}/0.jpg",
        f"https://cdn.takao.com.br/images-mult-prod/750/{codigo}/1.jpg",
        f"https://cdn.takao.com.br/images-mult-prod/750/{codigo}/0.jpg",
        f"https://takao.blob.core.windows.net/images-mult-prod/1000/{codigo}/1.jpg",
        f"https://takao.blob.core.windows.net/images-mult-prod/1000/{codigo}/0.jpg",
        f"https://takao.blob.core.windows.net/images-mult-prod/750/{codigo}/1.jpg",
        f"https://takao.blob.core.windows.net/images-mult-prod/750/{codigo}/0.jpg",
        "break"
    ]
    local_salvar = rf'{codigo.replace(" ", "")}.jpg'

    for l in links:
        if l == "break":
            lista_erros.append(codigo)
            
        if not baixar_imagem(l, local_salvar):
            continue
        else:
            break
