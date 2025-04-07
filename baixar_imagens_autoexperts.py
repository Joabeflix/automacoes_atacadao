import requests
import pandas as pd
import os

from tkinter import *
from tkinter import filedialog

# Função para obter o token de acesso
def get_access_token(client_key, client_secret):
    token_url = 'https://api.intelliauto.com.br/v1/login'
    token_payload = {
        'clientKey': client_key,
        'clientSecret': client_secret
    }
    token_response = requests.post(token_url, json=token_payload)
    if token_response.status_code == 200:
        return token_response.json().get('accessToken')
    return None

# Função para baixar e salvar a imagem dado o partNumber
def download_image(part_number, access_token, output_dir):
    url = f'https://api.intelliauto.com.br/v1/produtos/partnumber/{part_number}'
    headers = {'accept': 'application/json', 'Authorization': f'Bearer {access_token}'}
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        if 'data' in data and data['data']:
            imagens = data['data'][0].get('imagens')
            if imagens:
                image_url = imagens[0]['url']
                image_filename = os.path.join(output_dir, f'{part_number}.jpg')
                with open(image_filename, 'wb') as f:
                    f.write(requests.get(image_url).content)
                return image_filename
    return None

# Função para lidar com o botão de seleção de arquivo
def select_file():
    global file_path_entry
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
    file_path_entry.delete(0, END)
    file_path_entry.insert(0, file_path)

# Função para executar o processo
def execute_process():
    # Obter os valores dos tokens e local do arquivo da interface
    client_key = client_key_entry.get()
    client_secret = client_secret_entry.get()
    file_path = file_path_entry.get()

    # Obter token de acesso
    access_token = get_access_token(client_key, client_secret)

    if access_token:
        # Ler o arquivo Excel com os códigos de peças
        df = pd.read_excel(file_path)

        # Criar um diretório para salvar as imagens na área de trabalho
        desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        output_dir = os.path.join(desktop_path, 'imagens_autoparts')
        os.makedirs(output_dir, exist_ok=True)

        # Baixar e salvar as imagens
        df['Imagem'] = df['partNumber'].apply(lambda x: download_image(x, access_token, output_dir))

        print("Imagens baixadas e salvas em:", output_dir)
    else:
        print("Falha ao obter token de acesso.")

# Criar a interface
root = Tk()
root.title("Baixar Imagens de Produtos")

# Rótulos e campos de entrada para os tokens e o local do arquivo
Label(root, text="Client Key:").grid(row=0, column=0, sticky=W)
client_key_entry = Entry(root)
client_key_entry.grid(row=0, column=1, padx=5, pady=5)

Label(root, text="Client Secret:").grid(row=1, column=0, sticky=W)
client_secret_entry = Entry(root)
client_secret_entry.grid(row=1, column=1, padx=5, pady=5)

Label(root, text="Local da Planilha:").grid(row=2, column=0, sticky=W)
file_path_entry = Entry(root)
file_path_entry.grid(row=2, column=1, padx=5, pady=5)

Button(root, text="Selecionar Arquivo", command=select_file).grid(row=2, column=2, padx=5, pady=5)

Button(root, text="Executar", command=execute_process).grid(row=3, columnspan=2, pady=10)

root.mainloop()
