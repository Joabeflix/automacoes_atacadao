import pandas as pd

"""

FALTA FAZER A PARTE DE USAR A PLANILHA


"""


def datas_separadas(ano_inicio, qtd_de_datas):
    lista = []
    inicial = 0 # 1, 2, 3, 4, 5, 6, 7...
    while inicial < qtd_de_datas:
        if inicial == 0:
            valor_data = ano_inicio
            lista.append(valor_data)
            inicial+=1
            continue

        valor_data = ano_inicio+inicial
        lista.append(valor_data)
        inicial+=1

    return lista


# 2000, 2001, 2002, 2003 ------> 4 qtd
ano_inicio = 1956
ano_fim = 1980
qtd_de_datas = ano_fim - ano_inicio + 1

x = datas_separadas(ano_inicio, qtd_de_datas)
datas = ', '.join([str(conversor) for conversor in x])
print(datas, type(datas))








