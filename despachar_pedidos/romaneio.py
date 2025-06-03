import os
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import StringVar
from despachar_pedidos.tratamento_planilha_romaneio import TratamentoPlanilhaMercadoLivre


class ConferenciaApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Conferência de saída - Mercado Livre")
        self.master.geometry("933x745")

        self.dados = self.carregar_dados()

        self.label_titulo = ttk.Label(master, text="Status da Conferência", font=("Segoe UI", 18, "bold"))
        self.label_titulo.place(x=20, y=10)

        self.lista_status = ttk.Text(master, width=80, height=20, font=("Segoe UI", 10))
        self.lista_status.place(x=20, y=65)

        self.codigo_var = StringVar()
        self.entry_codigo = ttk.Entry(master, textvariable=self.codigo_var, width=40, font=("Segoe UI", 10))
        self.entry_codigo.place(x=20, y=650)
        self.entry_codigo.bind("<Return>", self.conferir_codigo)

        self.botao = ttk.Button(master, text="Conferir", bootstyle='success-outline', command=self.conferir_codigo)
        self.botao.place(x=478, y=653)

        self.label_mensagem = ttk.Label(master, text="", font=("Segoe UI", 10), foreground="blue")
        self.label_mensagem.place(x=20, y=700)

        self.atualizar_lista()

    def carregar_dados(self):
        app = TratamentoPlanilhaMercadoLivre(
            local_planilha=r'C:\Users\joabe\Desktop\dados_meli.xlsx',
            nome_aba_cod_rastreiro='Número de rastreamento',
            nome_aba_nome_cliente='Dados pessoais ou da empresa'
        )
        return app._criar_dicionario()

    def atualizar_lista(self):
        self.lista_status.delete("1.0", "end")
        for codigo, info in self.dados.items():
            status = "✅ CONFIRMADO" if info["status_conferencia"] else "⏳ PENDENTE"
            self.lista_status.insert("end", f"{codigo} - {status} - {info['nome_cliente']}\n")

    def conferir_codigo(self, event=None):
        codigo = self.codigo_var.get().strip()
        if not codigo:
            return

        if codigo in self.dados:
            if not self.dados[codigo]["status_conferencia"]:
                self.dados[codigo]["status_conferencia"] = True
                self.mensagem(f"✅ {codigo} conferido com sucesso!")
            else:
                self.mensagem(f"⚠️ {codigo} já foi conferido anteriormente.")
        else:
            self.mensagem(f"❌ Código {codigo} não encontrado na lista!")

        self.codigo_var.set("")
        self.atualizar_lista()

        if all(info["status_conferencia"] for info in self.dados.values()):
            self.mensagem("✅ Todos os itens foram conferidos com sucesso!")

    def mensagem(self, texto):
        self.label_mensagem.config(text=texto)


if __name__ == "__main__":
    root = ttk.Window(themename="cosmo")
    app = ConferenciaApp(root)
    root.mainloop()
