import requests
from utils.utils import texto_no_console

class TOTSVSApi:
    def __init__(self, username, password):
        self.username=username
        self.password=password
        self.url='https://atacadao186732.protheus.cloudtotvs.com.br:10357/rest/'

    def retorno_pedido_api(self, numero_nota):
        resposta = requests.get(f'{self.url}{numero_nota}', auth=(self.username, self.password))
        
        if resposta.status_code == 200:
            texto_no_console('Conexão com a API do Protheus feita com sucesso.')
            return resposta.json()
        texto_no_console('Erro na conexão com a API do Protheus.')
        return None



            
if __name__ == '__main__':
    app = TOTSVSApi(
        username='ecommerce',
        password='123456'
    )

    

