import pandas as pd
import time


lista_de_meses = {
    "vend01": 1,
    "vend02": 2,
    "vend03": 3,
    "vend04": 4,
    "vend05": 5,
    "vend06": 6,
    "vend07": 7,
    "vend08": 8,
    "vend09": 9,
    "vend10": 10,
    "vend11": 11,
    "vend12": 12   
}

local_planilha = r"C:\Users\joab.alves\Downloads\CAIO - GIRO 2024 MES A MES.xlsx"
df = pd.read_excel(local_planilha, sheet_name="0101-M56")

lista_de_dados = []

# Percorrer linha por linha
for index, row in df.iterrows():
    valor_coluna_a = row.iloc[0] 
    linha = row.iloc[1:].to_dict()  
    lista_de_dados.append({int(valor_coluna_a): linha})



lista_sem_zeros = []


for x in lista_de_dados:

    linha = list(x.values())[0] 


    lista_sem_zero = {k: v for k, v in linha.items() if v != 0}


    lista_sem_zeros.append({list(x.keys())[0]: lista_sem_zero})

    # print(f"Valores sem zero para {list(x.keys())[0]}: {lista_sem_zero}")


lista_final_de_dados = []

for x in lista_sem_zeros:
    
    somente_dados = list(x.values())[0]
    sku = int(list(x.keys())[0])
    meses = somente_dados.keys()

    # print(sku)

    for mes, qtd in zip(meses, somente_dados):
        # print(m, somente_dados[qtd])
        # print(f'Mês: {lista_de_meses.get(m)}')
        lista_final_de_dados.append([sku, lista_de_meses[mes], somente_dados[qtd]])


df_novo = pd.DataFrame(lista_final_de_dados, columns=['Sku', 'Mês', 'Quantidade'])

df_novo.to_excel('0101-M56.xlsx', index=False)
