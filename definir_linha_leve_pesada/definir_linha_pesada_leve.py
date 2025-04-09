import pandas as pd
import time

exel_lista_veiculos = pd.read_excel(r"C:\Users\joab.alves\Desktop\plan_lista_linhas.xlsx", sheet_name='a')
exel_alterar = pd.read_excel(r"C:\Users\joab.alves\Desktop\plan_lista_linhas.xlsx", sheet_name='b')



lista_de_veiculos = [v[0] for v in exel_lista_veiculos.values.tolist()]
lista_nomes_anuncios = exel_alterar['nome']




lista_final = []

def verificadora(lista_veiculos, nome):
    nome = str(nome).upper()
    for veiculo in lista_veiculos:
        veiculo = str(veiculo).upper()
        if veiculo in nome:
            print(f'Linha Pesada {nome}')
            return 'PESADA'
        else:
            continue
    print(f'Linha Leve {nome}')
    return 'LEVE'


def main():
    for nome in lista_nomes_anuncios:
        lista_final.append(verificadora(lista_de_veiculos, nome))        
    
    exel_alterar['Linha'] = lista_final
    slv = exel_alterar.to_excel('teste.xlsx', index=False)


main()



