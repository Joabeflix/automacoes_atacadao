import pandas as pd
from utils.utils import texto_no_console

class TratamentoPlanilhaPedidosNf:
    def __init__(self, caminho_arquivo, aba_pedido, aba_nf):
        self.caminho_arquivo = caminho_arquivo
        self.aba_pedido = aba_pedido
        self.aba_nf = aba_nf
        self.dicionario_pedidos = self._carregar_dados()

    def _carregar_dados(self):
        try:
            planilha = pd.read_excel(self.caminho_arquivo)
            pedidos = list(planilha[self.aba_pedido])
            notas = list(planilha[self.aba_nf])
            return {
                str(self._acertar_pedido(p)): str(self._acertar_nota(n))
                for p, n in zip(pedidos, notas)
            }
        except FileNotFoundError:
            texto_no_console('Erro: Arquivo da planilha não encontrado. Verifique o caminho informado.')
            return {}

    def _acertar_pedido(self, pedido):
        # Implementações futuras
        return pedido

    def _acertar_nota(self, nota):
        # Implementações futuras
        return nota

    def get_dicionario(self):
        return self.dicionario_pedidos or ''

# Exemplo de uso
if __name__ == '__main__':
    app = TratamentoPlanilhaPedidosNf(
        caminho_arquivo='despachar_pedidos/pedidos_x_notas.xlsx',
        aba_pedido='Pedido',
        aba_nf='Nota'
    )
    print(app.get_dicionario())
