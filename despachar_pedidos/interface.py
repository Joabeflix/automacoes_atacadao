import pandas as pd
import tkinter as tk
from utils.utils import tela_aviso, limpar_prompt
from despachar_pedidos.tratamento_planilha import TratamentoPlanilhaPedidosNf
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import StringVar

dicionario_notas = TratamentoPlanilhaPedidosNf(
    local_planilha=r'despachar_pedidos\pedidos_x_notas.xlsx',
    nome_aba_pedido='Pedido',
    nome_aba_nf='Nota'
).retorno_dicionario()

def remover_zero_esquerda(obj):
    if not obj:
        return ''
    return str(int(obj))

def extrair_numero_nota(chave_acesso):
    if not chave_acesso:
        log_mensagem("Chave de acesso vazia.")
        return False
    if len(chave_acesso) != 44 or not chave_acesso.isdigit():
        log_mensagem(f"Chave de acesso inválida: {chave_acesso}")
        return False
    numero_nota = chave_acesso[25:34]
    return remover_zero_esquerda(numero_nota)

# Janela principal
janela = ttk.Window(themename='darkly')
janela.title("Validador de NF x Pedido")
janela.geometry("650x450")
janela.resizable(False, False)

# Variáveis
chave_var = StringVar()
pedido_var = StringVar()

# Caixa de log (maior)
caixa_log = tk.Text(janela, height=12, width=78, wrap='word', state='disabled', bg='#1e1e1e', fg='white')
caixa_log.place(x=30, y=180)

scroll_log = ttk.Scrollbar(janela, command=caixa_log.yview)
scroll_log.place(x=610, y=180, height=200)
caixa_log.configure(yscrollcommand=scroll_log.set)

# Função de log
def log_mensagem(msg):
    caixa_log.configure(state='normal')
    if isinstance(msg, list):
        for linha in msg:
            caixa_log.insert(tk.END, f"{linha}\n")
    else:
        caixa_log.insert(tk.END, f"{msg}\n")
    caixa_log.configure(state='disabled')
    caixa_log.see(tk.END)

# Lógica principal
def verificar_relacao(event=None):
    chave = chave_var.get().strip()
    pedido_raw = pedido_var.get().strip()

    nota = extrair_numero_nota(chave)
    pedido = remover_zero_esquerda(pedido_raw)

    if not nota or not pedido:
        return

    if dicionario_notas.get(pedido) == nota:
        log_mensagem(['\n', '✅ Pedido confirmado.'])
        log_mensagem(f'NF: {nota} / Pedido: {pedido}')
    else:
        nota_relacionada = dicionario_notas.get(pedido)
        if nota_relacionada:
            mensagem = (
                f"❌ A nota fiscal ({nota}) não é relacionada com o pedido {pedido}.\n"
                f"O pedido {pedido} está relacionado com a nota {nota_relacionada}."
            )
        else:
            mensagem = f'❌ A nota fiscal ({nota}) não bateu com o pedido!!!'
        tela_aviso('Diferença', mensagem, tipo='erro')
        log_mensagem(mensagem)

    # Limpa e foca para próxima leitura
    chave_var.set("")
    pedido_var.set("")
    entry_chave.focus()

# Labels e Entradas
ttk.Label(janela, text="Chave de Acesso:", font=("Segoe UI", 10)).place(x=40, y=30)
entry_chave = ttk.Entry(janela, textvariable=chave_var, width=50)
entry_chave.place(x=170, y=30)
entry_chave.focus()

ttk.Label(janela, text="Pedido:", font=("Segoe UI", 10)).place(x=40, y=80)
entry_pedido = ttk.Entry(janela, textvariable=pedido_var, width=25)
entry_pedido.place(x=170, y=80)

# Botão (depois da definição da função)
ttk.Button(janela, text="Verificar", width=20, command=verificar_relacao).place(x=250, y=130)

# Eventos para navegação rápida
entry_chave.bind("<Return>", lambda e: entry_pedido.focus())
entry_pedido.bind("<Return>", verificar_relacao)

# Inicia janela
janela.mainloop()
