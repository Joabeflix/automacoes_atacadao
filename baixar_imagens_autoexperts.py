import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import requests
import os

CLIENT_KEY = '222bee82-0b5f-4ec9-bc20-0e09389c2f05'
CLIENT_SECRET = 'f3cbf1bd243e645d44583189af45c08e'

def gerar_token():
    token_url = 'https://api.intelliauto.com.br/v1/login'
    payload = {'clientKey': CLIENT_KEY, 'clientSecret': CLIENT_SECRET}
    response = requests.post(token_url, json=payload)
    if response.status_code == 200:
        return response.json().get('accessToken')
    else:
        raise Exception("Erro ao obter token")


def baixar_imagem(part_number, token, pasta_destino='imagens'):
    url = f'https://api.intelliauto.com.br/v1/produtos/partnumber/{part_number}'
    headers = {'accept': 'application/json', 'Authorization': f'Bearer {token}'}
    response = requests.get(url, headers=headers)

    if response.status_code == 401:
        raise Exception("Token expirado ou inválido")

    if response.status_code == 200:
        data = response.json()
        imagens = data.get('data', [{}])[0].get('imagens', [])
        if imagens:
            url_imagem = imagens[0].get('url')
            if url_imagem:
                img_response = requests.get(url_imagem)
                if img_response.status_code == 200:
                    os.makedirs(pasta_destino, exist_ok=True)
                    caminho_arquivo = os.path.join(pasta_destino, f'{part_number}.jpg')
                    with open(caminho_arquivo, 'wb') as f:
                        f.write(img_response.content)
                    print(f'Imagem salva: {caminho_arquivo}')
                else:
                    print(f'Erro ao baixar imagem de {part_number}')
            else:
                print(f'Nenhuma URL de imagem para {part_number}')
        else:
            print(f'Sem imagens para {part_number}')
    else:
        print(f'Erro na requisição do produto {part_number}')


def selecionar_arquivo():
    caminho_arquivo = filedialog.askopenfilename(filetypes=[("Planilhas Excel", "*.xlsx")])
    if not caminho_arquivo:
        return

    try:
        df = pd.read_excel(caminho_arquivo)
        if 'codigo' not in df.columns:
            messagebox.showerror("Erro", "A coluna 'codigo' não foi encontrada.")
            return

        lista_codigos = df['codigo'].dropna().astype(str).tolist()
        token = gerar_token()

        for cod in lista_codigos:
            baixar_imagem(cod, token)

        messagebox.showinfo("Concluído", "Download das imagens finalizado.")

    except Exception as e:
        messagebox.showerror("Erro", str(e))


# Interface gráfica
root = tk.Tk()
root.title("Baixar Imagens de Produtos")
root.geometry("400x150")

label = tk.Label(root, text="Selecione a planilha com a coluna 'codigo':")
label.pack(pady=10)

botao = tk.Button(root, text="Selecionar Arquivo Excel", command=selecionar_arquivo)
botao.pack(pady=10)

root.mainloop()
