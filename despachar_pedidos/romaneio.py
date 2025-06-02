import os
import time
from despachar_pedidos.tratar_exel_romaneio import TratamentoPlanilhaMercadoLivre
app = TratamentoPlanilhaMercadoLivre(
    local_planilha=r'C:\Users\joab.alves\Desktop\exel_meli.xlsx',
    nome_aba_cod_rastreiro='Número de rastreamento',
    nome_aba_nome_cliente='Dados pessoais ou da empresa'
)
print(app._criar_dicionario())

# Seus dados
dados = app._criar_dicionario()

def limpar_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_status(dados):
    print("=== STATUS DA CONFERÊNCIA ===")
    for codigo, info in dados.items():
        status = "✅ CONFIRMADO" if info['status_conferencia'] else "⏳ PENDENTE"
        print(f"{codigo} - {status} - {info['nome_cliente']}")
    print("\nDigite o código (ou 'sair' para encerrar)\n")

while True:
    limpar_console()
    exibir_status(dados)

    if all(info['status_conferencia'] for info in dados.values()):
        print("✅ Todos os itens foram conferidos com sucesso!")
        break

    codigo_input = input(">>> Código: ").strip()

    if codigo_input.lower() == 'sair':
        print("Encerrando conferência...")
        break

    codigo_input = f'MEL{codigo_input}FMDOF01'

    if codigo_input in dados:
        if not dados[codigo_input]['status_conferencia']:
            dados[codigo_input]['status_conferencia'] = True
            print(f"\n✅ {codigo_input} conferido com sucesso!")
        else:
            print(f"\n⚠️  {codigo_input} já foi conferido anteriormente.")
    else:
        print(f"\n❌ Código {codigo_input} não está na lista de conferência!")

