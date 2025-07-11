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
    return ', '.join([str(conversor) for conversor in lista])
ano_inicio = 2000
ano_fim = 2025
qtd_de_datas = ano_fim - ano_inicio + 1
print(datas_separadas(ano_inicio, qtd_de_datas))


def datas_separadas_2(ano_inicio, ano_fim):
    return ', '.join([f'{x + ano_inicio}' for x in range(ano_fim-ano_inicio+1)])
print(datas_separadas_2(ano_inicio=2000, ano_fim=2025))
