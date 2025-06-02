import tkinter as tk
from utils.utils import texto_no_console, tela_aviso, limpar_prompt
from despachar_pedidos.tratamento_planilha import TratamentoPlanilhaPedidosNf
texto_no_console('\n')

dicionario_notas = TratamentoPlanilhaPedidosNf(
    local_planilha=r'despachar_pedidos\pedidos_x_notas.xlsx',
    nome_aba_pedido='Pedido',
    nome_aba_nf='Nota'
)

dicionario_notas = dicionario_notas.retorno_dicionario()

    

def remover_zero_esquerda(obj):
    if not obj:
        return ''
    return str(int(obj))

def extrair_numero_nota(chave_acesso):

    if not chave_acesso:
        texto_no_console("Chave de acesso vazia.")
        return False
    if len(chave_acesso) != 44 or not chave_acesso.isdigit():
        texto_no_console(f"Chave de acesso inválida: {chave_acesso}")
        return False

    numero_nota = chave_acesso[25:34]
    return remover_zero_esquerda(numero_nota)

while True:
    entrada_nota = input('>>> Chave de acesso: ')
    nota = extrair_numero_nota(entrada_nota)

    if not nota:
        continue

    entrada_pedido = remover_zero_esquerda(input('>>> Pedido: '))
    pedido = remover_zero_esquerda(entrada_pedido)

    if dicionario_notas.get(pedido) == nota:
        texto_no_console(['\n', 'Pedido confirmado.'])
        texto_no_console(f'(NF: {nota} / PEDIDO: {pedido})')
    
    else:
        if dicionario_notas.get(pedido):
            mensagem = f"A nota fiscal ({nota}) não é relacionada com o pedido informado {(pedido)}.\nO pedido {pedido} é relacionado com a nota {dicionario_notas.get(pedido)}"
            
            tela_aviso('Diferença', mensagem, tipo='erro')
            continue
        tela_aviso('Diferença', f'A nota fiscal ({nota}) não bateu com o pedido!!!', 'erro')
    
    texto_no_console('_')