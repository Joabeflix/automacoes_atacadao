import pandas as pd


planilha = pd.read_excel('x.xlsx', sheet_name='dados')

coluna_alterar = planilha['nome padrao']


lista_nova = []
for x in coluna_alterar:
    lista_nova.append(x[::-1])


planilha['coluna_nova'] = lista_nova


planilha.to_excel('planilhja.xlsx')



