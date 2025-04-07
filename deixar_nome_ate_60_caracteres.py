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
        "  ": " ",
    }

    def acertar_nomes(x):
        return str(x).upper().replace("  ", " ")
    
    def verificar_tamanho(nome):
        return True if len(nome) < 61 else False
    
    nome_produto = acertar_nomes(nome_produto)
    codigo_produto = acertar_nomes(codigo_produto)
    marca = acertar_nomes(marca)
    
    nome_novo = nome_produto.replace("  ", " ")

    if verificar_tamanho(nome_novo):
        return nome_novo.capitalize()
    
    nome_novo = nome_novo.replace(codigo_produto, "")
    nome_novo = nome_novo.replace("  ", " ")

    if verificar_tamanho(nome_novo):
        return nome_novo.capitalize()
    
    nome_novo = nome_novo.replace(marca, "")
    nome_novo = nome_novo.replace("  ", " ")

    if verificar_tamanho(nome_novo):
        return nome_novo.capitalize()
    
    for palavra in palavras_para_substituir:
        if palavra not in nome_novo:
            continue
        if verificar_tamanho(nome_novo):
            return nome_novo.capitalize()
        
        nome_novo = nome_novo.replace(palavra, palavras_para_substituir.get(palavra))
        return nome_novo.capitalize()
    




