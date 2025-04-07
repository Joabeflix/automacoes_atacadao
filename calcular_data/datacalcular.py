from datetime import datetime
import pandas as pd
import time



def calcular(data_x, data_y):

    # Converter as strings de datas para objetos datetime
    formato = "%d/%m/%Y"
    data_x_dt = datetime.strptime(data_x, formato)
    data_y_dt = datetime.strptime(data_y, formato)

    # Calcular a diferença entre as datas
    diferenca = data_y_dt - data_x_dt

    # Exibir a quantidade de dias corridos
    dias_corridos = diferenca.days

    return dias_corridos

planilha = pd.read_excel("planilha_data.xlsx", sheet_name="Planilha1" )

coluna_data_inicial = planilha['Cadastro']
coluna_data_final = planilha['Venda']


coluna_diferenca = []

for data_inicial, data_final in zip(coluna_data_inicial, coluna_data_final):

    dias = calcular(data_inicial, data_final)
    coluna_diferenca.append(dias)

planilha['Dias'] = coluna_diferenca

planilha.to_excel('Planilha_nova.xlsx', index=False)
print('Finalizado')
