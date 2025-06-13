import pandas as pd
import time
import os

exel_lista_veiculos = pd.read_excel(r"definir_linha_leve_pesada\plan_lista_linhas.xlsx", sheet_name='a')
exel_alterar = pd.read_excel(r"definir_linha_leve_pesada\plan_lista_linhas.xlsx", sheet_name='b')



lista_de_veiculos = [v[0] for v in exel_lista_veiculos.values.tolist()]
lista_nomes_anuncios = exel_alterar['aplic']

lista_final = []



def verificadora(lista_veiculos, nome):
    nome = str(nome).upper()
    for veiculo in lista_veiculos:

        veiculo = str(veiculo).upper()
        if veiculo in nome:
    
            return 'PESADA'
        else:
            continue

    return 'LEVE'


def main():
    total = len(lista_nomes_anuncios)
    contagem = 1
    for nome in lista_nomes_anuncios:
        lista_final.append(verificadora(lista_de_veiculos, nome))   
        os.system('cls')
        print(f'Feito: {contagem}/{total}')
        contagem+=1     
    
    exel_alterar['Linha'] = lista_final
    slv = exel_alterar.to_excel(rf'definir_linha_leve_pesada\Anúncios Linha Pesada.xlsx', index=False)


main()



