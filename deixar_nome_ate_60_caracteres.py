def deixar_nome_ate_60_caracteres(nome_produto, codigo_produto, marca):

    palavras_para_substituir = {
        "DIANTEIRO": "DIANT",
        "DIANTEIRA": "DIANT",
        "TRASEIRO": "TRAS",
        "TRASEIRA": "TRAS",
        "DIREITA": "DIR",
        "DIREITO": "DIR",
        "ESQUERDA": "ESQ",
        "ESQUERDO": "ESQ",
        "ESQ DIR": "",
        "DIR ESQ": "",
        "Esquerdo/Direito": "Esq/Dir",
        "  ": " "
    }

    def acertar_nomes(x):
        return str(x).upper().replace("  ", " ")
    
    def verificar_tamanho(nome):
        return True if len(nome) < 61 else False
    
    def retorno_final(x):
        return x.title().rstrip()
    
    nome_produto = acertar_nomes(nome_produto)
    codigo_produto = acertar_nomes(codigo_produto)
    marca = acertar_nomes(marca)
    
    nome_novo = nome_produto.replace("  ", " ")

    if verificar_tamanho(nome_novo):
        return retorno_final(nome_novo)
    
    nome_novo = nome_novo.replace(codigo_produto, "")
    nome_novo = nome_novo.replace("  ", " ")

    if verificar_tamanho(nome_novo):
        return retorno_final(nome_novo)
    
    nome_novo = nome_novo.replace(marca, "")
    nome_novo = nome_novo.replace("  ", " ")

    if verificar_tamanho(nome_novo):
        return retorno_final(nome_novo)
    
    for palavra in palavras_para_substituir:
        if palavra not in nome_novo:
            continue
        if verificar_tamanho(nome_novo):
            return retorno_final(nome_novo)
        nome_novo = nome_novo.replace(palavra, palavras_para_substituir.get(palavra))

    return retorno_final(nome_novo)



def funcao_geral(lista_nome, lista_marca, lista_codigo):

    retorno = []

    for v_nome, v_marca, v_codigo in zip(lista_nome, lista_marca, lista_codigo):
        data = deixar_nome_ate_60_caracteres(nome_produto=v_nome, codigo_produto=v_codigo, marca=v_marca)
        if data == 'None':
            return retorno
        retorno.append(data)

    return retorno

_lista_nome = [x[0] for x in xl("I2:I1000").values]
_lista_marca = [x[0] for x in xl("H2:I1000").values]
_lista_codigo = [x[0] for x in xl("G2:I1000").values]

funcao_geral(lista_nome=_lista_nome, lista_marca=_lista_marca, lista_codigo=_lista_codigo)



