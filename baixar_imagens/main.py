import requests
import pandas as pd
import time
import os

time.sleep(10)
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



planilha = pd.read_excel(rf'C:\Users\joab.alves\Desktop\automacoes_atacadao\baixar_imagens\Links.xlsx')
lista_links = planilha['link']
lista_nomes = planilha['nome']

os.chdir(rf'C:\Users\joab.alves\Desktop\automacoes_atacadao\baixar_imagens\imagens')
lista_erros = []
lista_imagens_baixadas = os.listdir()

for l, n in zip(lista_links, lista_nomes):
    local_salvar = rf'{n}.jpg'
    if local_salvar in lista_imagens_baixadas:
        continue
    if baixar_imagem(url=l, local_salvar=local_salvar):
        continue

    lista_erros.append(n)


if lista_erros:
    print('\n\n ---------->|ERROS|<----------')
    for err in lista_erros:
        print(f'{err}')

   
