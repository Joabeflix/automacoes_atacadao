import pandas as pd
import tkinter as tk
from utils.utils import texto_no_console, tela_aviso
from despachar_pedidos.tratamento_planilha import TratamentoPlanilha





dicionario_notas = TratamentoPlanilha(
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
        raise ValueError("Chave de acesso vazia.")
    if len(chave_acesso) != 44 or not chave_acesso.isdigit():
        raise ValueError(f"Chave de acesso inválida: {chave_acesso}")

    numero_nota = chave_acesso[25:34]
    return remover_zero_esquerda(numero_nota)

while True:
    entrada_nota = input('>>> Chave de acesso: ')
    nota = extrair_numero_nota(entrada_nota)

    entrada_pedido = remover_zero_esquerda(input('>>> Pedido: '))
    pedido = remover_zero_esquerda(entrada_pedido)

    if dicionario_notas.get(pedido) == nota:
        texto_no_console(['\n', 'Pedido confirmado.'])
        texto_no_console(f'(NF: {nota} / PEDIDO: {pedido})')
    
    else:
        tela_aviso('Diferença', f'A nota fiscal não bateu com o pedido!!! ({nota} --- {pedido})', tipo='erro')
    
    texto_no_console('_')