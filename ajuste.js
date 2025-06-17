function main(workbook: ExcelScript.Workbook) {
  let selectedSheet = workbook.getActiveWorksheet();
  selectedSheet.getRange("C:C").insert(ExcelScript.InsertShiftDirection.right);
  selectedSheet.getRange("C1").setValue("posição");
  selectedSheet.getRange("D:D").insert(ExcelScript.InsertShiftDirection.right);
  selectedSheet.getRange("D1").setValue("nome padrao");
  selectedSheet.getRange("E:E").insert(ExcelScript.InsertShiftDirection.right);
  selectedSheet.getRange("E1").setValue("veiculo");
  selectedSheet.getRange("I1").setValue("nome anuncio");
  selectedSheet.getRange("J1").setValue("nome ate 60");
  selectedSheet.getRange("K1").setValue("Descrição");
  selectedSheet.getRange("L1").setValue("Link Img");

  // Configuração do nome do anúncio
  selectedSheet.getRange("I2").setFormulaLocal('=SE(A2=0;"";PRI.MAIÚSCULA(ARRUMAR(D2&" Compativel "&E2&" "&C2&" "&H2&" "&G2)))');


  // Configuração do link das imagens
  // Exemplo de link: https://samarcmkt.s3.us-east-2.amazonaws.com/IMG/0002KE-2.jpg
  // O padrão vai ser === Se o código do produto deveria
  // '=SE(A2=0;"";"https://samarcmkt.s3.us-east-2.amazonaws.com/IMG/"&L2&".jpg"'

  const formulaImagem = `=SE(A2=0;"";"https://samarcmkt.s3.us-east-2.amazonaws.com/IMG/" & H2 & "-" & SUBSTITUIR(G2; "/"; "-") & ".jpg, https://samarcmkt.s3.us-east-2.amazonaws.com/IMG/" & H2 & "-" & SUBSTITUIR(G2; "/"; "-") & "-2.jpg, https://samarcmkt.s3.us-east-2.amazonaws.com/IMG/" & H2 & "-" & SUBSTITUIR(G2; "/"; "-") & "-3.jpg")`;

  selectedSheet.getRange("L2").setFormulaLocal(formulaImagem);


  const codigo_py_nome_ate_60 = `
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
    

nome = xl("I2")
marca = xl("H2")
modelo = xl("G2")

deixar_nome_ate_60_caracteres(nome_produto=nome, marca=marca, codigo_produto=modelo)
`


const codigo_py_definir_lado_posicao = `
""" Código feito para rodar no Python-Excel """
nome_anuncio = xl("B2")  # Célula do Excel

# Dicionários de busca
lados_dict = {
    "esq dir": ["Esquerdo", "Direito"],
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


# Resultado final
resultado = analisar_anuncio(nome_anuncio)
resultado
`


  selectedSheet.getRange("C2").setValue(`PY(${codigo_py_definir_lado_posicao})`);



  selectedSheet.getRange("J2").setValue(`PY(${codigo_py_nome_ate_60})`);
}
