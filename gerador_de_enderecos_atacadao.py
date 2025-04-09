import pandas as pd

def estilo_prateleira():
    faixa_1 = [f"{i:03}" for i in range(1, 33)] 
    faixa_2 = [f"{j:02}" for j in range(1, 25)]
    letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

    enderecos = [f"{n1}-{n2}-{letra}" for n1 in faixa_1 for n2 in faixa_2 for letra in letras]

    df = pd.DataFrame(enderecos, columns=["Endereço"])
    df.to_excel("enderecos_estoque_teste2.xlsx", index=False)

def enderecos_pd():
    faixa_1 = [x for x in range(6)]
    faixa_2 = [f"{x:02}" for x in range(1, 10)]
    letras = ['A', 'B', 'C', 'D']

    enderecos = [f"PD{n1}-{n2}-{letra}" for n1 in faixa_1 for n2 in faixa_2 for letra in letras]

    df = pd.DataFrame(enderecos, columns=["Endereço"])
    df.to_excel("enderecos_estoque_pd.xlsx", index=False)




enderecos_pd()
