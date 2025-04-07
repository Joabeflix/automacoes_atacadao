import re

""" Código feito para rodar no Python-Excel """
endereco = "01-01-B"
endereco = xl("K2") # Célula do Excel
#
#
#
#
#
padrao = r"^(?:\d{3}-\d{2}-[A-Z]|PD\d-\d{2}-[A-Z])$"

def corrigir_formato(codigo):
    if codigo.startswith("PD"):
        partes = codigo.split("-")
        if len(partes) == 3 and len(partes[0]) == 3:
            num1 = partes[1].zfill(2)
            return f"{partes[0]}-{num1}-{partes[2]}"
        return "Acertar"
    elif "-" in codigo:
        partes = codigo.split("-")
        if len(partes) == 3:
            num1 = partes[0].zfill(3)
            num2 = partes[1].zfill(2)
            return f"{num1}-{num2}-{partes[2]}"
        return "Acertar"
    return "Acertar"


def verificar_padrao():
    corrigido = corrigir_formato(endereco)
    if re.match(padrao, corrigido):
        return corrigido
    else:
        return "Acertar"

verificar_padrao()
