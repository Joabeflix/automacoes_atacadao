""" Código feito para rodar no Python-Excel """

posicoes = {
    "DIANTEIRA": "dianteiro",
    "DIANTEIRO": "dianteiro",
    " DIANT ": "dianteiro",
    "TRASEIRA": "traseiro",
    "TRASEIRO": "traseiro",
    " TRAS ": "traseiro"
}


def pegar_posicao(x) -> str:
    for p in posicoes.keys():
        if p not in str(x).upper():
            continue
        return posicoes.get(p)
    return ''



