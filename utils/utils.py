import json
import numpy as np
import os
from tkinter import messagebox
import re

def texto_no_console(obj):
    separadores = ['_', '*', '-', '#']
    if obj in separadores:
        print(obj * 30)
        return None
    if isinstance(obj, list):
        for t in obj:
            if t == '\n':
                print('\n')
                continue
            print(f'>>> {t}{'\n'}')
        return None
    print(f'>>> {obj}{'\n'}')

def alterar_valor_json(caminho_json, chave, novo_valor):
    with open(file=caminho_json, mode='r', encoding='utf8') as arquivo:
        dados = json.load(arquivo)
    dados[chave] = novo_valor
    with open(file=caminho_json, mode='w', encoding='utf8') as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=4)

def tela_aviso(titulo, mensagem, tipo):

    tipos = {
        "informacao": messagebox.showinfo,
        "erro": messagebox.showerror
    }
    if tipo in tipos.keys():
        return tipos.get(tipo)(title=titulo, message=mensagem)
    texto_no_console([
        f'Tipo de tela não cadastrado na função: {tipo}', 
        f'Tipos cadastrados: {list(tipos.keys())}'])

def converter_int64_para_int(obj):
    """ Se não for int64 ele retorna o valor original."""
    if isinstance(obj, np.int64):
        return int(obj)
    return obj

def limpar_prompt():
    os.system('cls')
