import pandas as pd
import requests



local_planilha = 'links_produtos.xlsx'

planilha = pd.read_excel(local_planilha)

links = planilha['Links']
codigo_produto = planilha['mpn']

lista_erros = []

for link, codigo in zip(links, codigo_produto):

    codigo_ = str(codigo).replace('/', '-')
    nome_imagem = f'imagens_produtos/{codigo_}.jpg'


    resposta = requests.get(link)
    if resposta.status_code == 200:
        with open(nome_imagem, 'wb') as imagem:
            imagem.write(resposta.content)
        print(f'Imagem do produto {codigo} salva com sucesso!')
    else:
        lista_erros.append(codigo)
    


for x in lista_erros:
    print(x)




