
import tkinter as tk
from tkinter import filedialog, Listbox
import os
import ttkbootstrap as ttk
import time

def listar_arquivos():
    pasta = filedialog.askdirectory()
    if pasta:
        listbox_arquivos.delete(0, tk.END)
        for arquivo in os.listdir(pasta):
            if arquivo.lower().endswith(".jnlp"):
                listbox_arquivos.insert(tk.END, os.path.join(pasta, arquivo))

def selecionar_arquivo():
    selecionado = listbox_arquivos.curselection()
    if selecionado:
        entry_arquivo.delete(0, tk.END)
        entry_arquivo.insert(0, listbox_arquivos.get(selecionado[0]))

def caminho_arquivo():
    caminho = entry_arquivo.get()
    
    if caminho:
        caminho = caminho.replace("\\", "/") 
        print(f"Arquivo selecionado: {caminho}")
        return caminho
        

def executar_javaws():
    arquivo_jnlp = caminho_arquivo()
    time.sleep(0.3)
    print('Dentro da Função')
    print(arquivo_jnlp)
    os.system(f"powershell -Command javaws {arquivo_jnlp}")


# Criando a janela principal
root = ttk.Window(themename="morph")
root.title("Gerenciador de assinador")
root.geometry("460x400")

# Criando widgets
frame = ttk.Frame(root, padding=10)
frame.pack(fill='both', expand=True)

btn_listar = ttk.Button(frame, text="Selecionar Pasta", command=listar_arquivos, bootstyle='info-outline')
btn_listar.pack(pady=5)

listbox_arquivos = Listbox(frame, height=10)
listbox_arquivos.pack(pady=5, fill='both', expand=True)

entry_arquivo = ttk.Entry(frame, width=50)
entry_arquivo.pack(pady=5, fill='x')

btn_selecionar = ttk.Button(frame, text="Selecionar Arquivo", command=selecionar_arquivo, bootstyle='primary-outline')
btn_selecionar.pack(pady=5)

btn_confirmar = ttk.Button(frame, text="Confirmar", command=executar_javaws, bootstyle='success-outline')
btn_confirmar.pack()

ttk.Label(text='By Joabe Alves da Luz :)').pack()

# Executando a aplicação
root.mainloop()
