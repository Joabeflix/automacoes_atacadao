import pandas as pd

def gerar_enderecos(estilo_usar, faixa_1, faixa_2, letras):

    faixa_1 = [x for x in range(6)]
    faixa_2 = [f"{j:02}" for j in range(1, 25)]
    letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

    estilos = {
        "faixas_plateleiras": [f"{n1}-{n2}-{letra}" for n1 in faixa_1 for n2 in faixa_2 for letra in letras],
        "faixas_pd": [f"PD{n1}-{n2}-{letra}" for n1 in faixa_1 for n2 in faixa_2 for letra in letras]
    }
    enderecos = estilos.get(estilo_usar)

    df = pd.DataFrame(enderecos, columns=['Endereço'])
    df.to_excel(f"enderecos_estoque_estilo_{estilo_usar}.xlsx", index=False)

faixas = {
    "faixas_plateleiras": {
        "faixa_1": [f"{i:03}" for i in range(17, 32)],
        "faixa_2": [f"{j:02}" for j in range(1, 25)],
        "letras": ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    },
    "faixas_pd": {
        "faixa_1": [x for x in range(6)],
        "faixa_2": [f"{x:02}" for x in range(1, 10)],
        "letras": ['A', 'B', 'C', 'D']
    }
}


faixa_usar = "faixas_pd"

faixas = faixas.get(faixa_usar)
gerar_enderecos(estilo_usar=faixa_usar, faixa_1=faixas['faixa_1'], faixa_2=faixas['faixa_2'], letras=faixas['letras'])








