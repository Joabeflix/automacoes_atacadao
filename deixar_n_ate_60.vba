Function retorno_final(x As String) As String
    retorno_final = StrConv(x, vbProperCase)
End Function

Function acertar_texto(x As String) As String
    Dim retorno As String
    retorno = Replace(Trim(UCase(x)), "  ", " ")
    
    Do While InStr(retorno, "  ") > 0:
        retorno = Replace(retorno, "  ", " ")
    Loop
    acertar_texto = retorno
End Function

Function verificar_tamanho(x As String) As Boolean
    verificar_tamanho = IIf(Len(x) > 60, True, False)
End Function

Function substituir_e_acertar(nome As String, subs As String, por As String)
    substituir_e_acertar = acertar_texto(Replace(nome, subs, por))
End Function



Function Principal(nome As String, codigo_produto As String, marca As String) As String
    Dim lista_substituicoes
    Set lista_substituicoes = CreateObject("Scripting.Dictionary")

    lista_substituicoes.Add "DIANTEIRA", "DIANT"
    lista_substituicoes.Add "DIANTEIRO", "DIANT"
    lista_substituicoes.Add "TRASEIRO", "TRAS"
    lista_substituicoes.Add "TRASEIRA", "TRAS"
    lista_substituicoes.Add "DIREITA", "DIR"
    lista_substituicoes.Add "ESQUERDA", "ESQ"
    lista_substituicoes.Add "DIREITO", "DIR"
    lista_substituicoes.Add "ESQUERDO", "ESQ"
    lista_substituicoes.Add "ESQ DIR", ""
    lista_substituicoes.Add "DIR ESQ", ""
    lista_substituicoes.Add "  ", " "
    lista_substituicoes.Add "DIANTEIRO", "DIANT"

    Dim nome As String
    nome = acertar_texto(nome)
    Dim codigo_produto As String
    codigo_produto = acertar_texto(codigo_produto)
    Dim marca As String
    marca = acertar_texto(marca)

    If verificar_tamanho(nome) Then
        Principal = retorno_final(nome)

    nome = substituir_e_acertar(nome, codigo_produto, "")

    If verificar_tamanho(nome) Then
        Principal = retorno_final(nome)

    nome = substituir_e_acertar(nome, marca, "")

    If verificar_tamanho(nome) Then
        Principal = retorno_final(nome)


    Dim palavra As Variant
    For Each palavra In lista_substituicoes.keys
        If InStr(nome, palavra) > 0 Then
            If verificar_tamanho(nome) Then
                nome = substituir_e_acertar(nome, palavra, lista_substituicoes(palavra))
            Else
                Principal = retorno_final(nome)
            End If
        End If
    Next palavra

    Principal = nome
