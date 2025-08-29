Function gerar_link(marca As String, codigo As String) As String
    
    ''https://samarcmkt.s3.us-east-2.amazonaws.com/IMG/0002KE-3.jpg
    
    Dim padrao_link As String
    padrao_link = "https://samarcmkt.s3.us-east-2.amazonaws.com/IMG/"
    Dim marca_codigo As String

    marca_codigo = marca & "-" & codigo

    gerar_link = padrao_link & marca_codigo & ".jpg," & _ 
                padrao_link & marca_codigo & "-2.jpg," & _
                padrao_link & marca_codigo & "-3.jpg"

End Function



