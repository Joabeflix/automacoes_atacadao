Function deixar_nome_ate_60_caracteres(Nome_produto As String, Codigo_produto As String, Marca As String) As String
    Dim palavrasParaSubstituir As Object
    Set palavrasParaSubstituir = CreateObject("Scripting.Dictionary")
    
    ' Definir as palavras e suas substituições
    ' PALAVRAS PADRÕES SUBSTITUIR
    
    palavrasParaSubstituir.Add "DIANTEIRO", "DIANT"
    palavrasParaSubstituir.Add "DIANTEIRA", "DIANT"
    palavrasParaSubstituir.Add "TRASEIRO", "TRAS"
    palavrasParaSubstituir.Add "TRASEIRA", "TRAS"
    palavrasParaSubstituir.Add "DIREITA", "DIR"
    palavrasParaSubstituir.Add "ESQUERDA", "ESQ"
    palavrasParaSubstituir.Add "DIREITO", "DIR"
    palavrasParaSubstituir.Add "ESQUERDO", "ESQ"
    palavrasParaSubstituir.Add "ESQ DIR", ""
    palavrasParaSubstituir.Add "DIR ESQ", ""
    palavrasParaSubstituir.Add "  ", " "
    palavrasParaSubstituir.Add "DIANTEIRO", "DIANT"
    
    ' Manipulação das strings
    Nome_produto = UCase(Trim(Replace(Nome_produto, "  ", " ")))
    Codigo_produto = UCase(Trim(Replace(Codigo_produto, "  ", " ")))
    Marca = UCase(Trim(Replace(Marca, "  ", " ")))
    
    Dim nomeNovo As String
    nomeNovo = Nome_produto

    ' Se o nome for maior que 60 caracteres, aplicar substituições
    If Len(Nome_produto) > 60 Then
        ' Remover o MPN se o nome for muito longo
        nomeNovo = Replace(Nome_produto, Codigo_produto, "")
        nomeNovo = Trim(Replace(nomeNovo, "  ", " "))
        
        ' Se ainda for maior que 60, remover a marca
        If Len(nomeNovo) > 60 Then
            nomeNovo = Replace(nomeNovo, Marca, "")
            nomeNovo = Trim(Replace(nomeNovo, "  ", " "))
            
            ' Se ainda for maior que 60, fazer substituições de padrões
            If Len(nomeNovo) > 60 Then
                Dim palavra As Variant
                For Each palavra In palavrasParaSubstituir.Keys
                    If InStr(nomeNovo, palavra) > 0 Then
                        nomeNovo = Replace(nomeNovo, palavra, palavrasParaSubstituir(palavra))
                    End If
                Next palavra
            End If
        End If
    End If
    
    ' Colocar cada palavra com a primeira letra maiúscula
    deixar_nome_ate_60_caracteres = Application.WorksheetFunction.Proper(nomeNovo)
End Function
