import pandas as pd

planilha = pd.read_excel('Anúncios Linha Pesada.xlsx')

coluna_aplicacao = planilha['aplic']

retorno = []

for nome in coluna_aplicacao: 
    retorno.append(str(nome).strip())


planilha['aplicacao acertada'] = retorno

planilha.to_excel('Anuncios_linha_pesada.xlsx', index=False)



