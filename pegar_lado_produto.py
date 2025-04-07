""" Código feito para rodar no Python-Excel """
nome_anuncio = xl("B2") # Célula do Excel
#
#
#
#
#
def definir_posicao():
    lista_posicoes = {
        " dir ": "Direito",
        " esq ": "Esquerdo",
        "esq dir": "Esquerdo/Direito",
        "dir esq": "Esquerdo/Direito"
    }
    
    for l in lista_posicoes.keys():
        if l in nome_anuncio.lower():
            return lista_posicoes.get(l)
    return ''
            
definir_posicao()
