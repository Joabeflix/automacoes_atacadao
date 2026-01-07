""" Código feito para rodar no Python-Excel """

lados_dict = {
    "esq dir": ["", "Direito"],
    "dir esq": ["Esquerdo", "Direito"],
    " dir ": ["Direito"],
    " esq ": ["Esquerdo"],
    "esquerdo": ["Esquerdo"],
    "direito": ["Direito"],
    "esquerda": ["Esquerdo"],
    "direita": ["Direito"],
    "esquerdo direito": ["Esquerdo/Direito"],
    "direito esquerdo": ["Esquerdo/Direito"],
    "esquerda direita": ["Esquerdo/Direito"],
    "direita esquerda": ["Esquerdo/Direito"]
}

posicoes_dict = {
    "DIANTEIRA": "dianteiro",
    "DIANTEIRO": "dianteiro",
    " DIANT ": "dianteiro",
    "TRASEIRA": "traseiro",
    "TRASEIRO": "traseiro",
    " TRAS ": "traseiro"
}


def analisar_anuncio(nome):
    nome = str(nome).lower()
    lados_encontrados = set()
    posicoes_encontradas = set()
    # Procurar lados
    for chave, valores in lados_dict.items():
        if chave in nome:
            lados_encontrados.update(valores)
    # Procurar posições
    for chave, valor in posicoes_dict.items():
        if chave.lower() in nome:
            posicoes_encontradas.add(valor)
    # Montagem do resultado final
    if not lados_encontrados and not posicoes_encontradas:
        return ''
    if not lados_encontrados:
        return ', '.join(sorted(posicoes_encontradas))
    if not posicoes_encontradas:
        return '/'.join(sorted(lados_encontrados))
    # Caso tenha ambos
    lados_str = '/'.join(sorted(lados_encontrados))
    posicoes_str = ', '.join(sorted(posicoes_encontradas))
    return f"{posicoes_str} {lados_str}"

def _main(lista_excel) -> list:
    retorno: list[str] = []
    for x in lista_excel:
        retorno.append(analisar_anuncio(x))
    return retorno


lista = [f'{x[0]}' for x in xl("B2:B687").values]


resultado = _main(lista_excel=lista)
resultado



# # Resultado final
# resultado = analisar_anuncio(nome_anuncio)
# resultado


