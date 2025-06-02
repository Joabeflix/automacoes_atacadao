import pandas as pd
from utils.utils import texto_no_console

class TratamentoPlanilha:
    def __init__(self, local_planilha, nome_aba_pedido, nome_aba_nf):
        self.local_planilha = local_planilha
        self.nome_aba_pedido = nome_aba_pedido
        self.nome_aba_nf = nome_aba_nf
        self.dicionario_pedido_notas = None

        try:
            planilha = pd.read_excel(local_planilha)
            lista_pedido, lista_nf = list(planilha[nome_aba_pedido]), list(planilha[nome_aba_nf])

            self.dicionario_pedido_notas = self._criar_dicionario(lista_pedido, lista_nf)
        except FileNotFoundError:
            texto_no_console('Erro ao ler a planilha. O arquivo não foi encontrado. Verifique o local do arquivo.')
            return None
        

    def retorno_dicionario(self):
        if self.dicionario_pedido_notas:
            return self.dicionario_pedido_notas
        return ''
            
    def _criar_dicionario(self, aba_pedido, aba_nf):
        
        dicionario = {}

        for p, n in zip(aba_pedido, aba_nf):
            dicionario[str(self._acertar_pedido(p))] = str(self._acertar_nota(n))
        return dicionario



    def _acertar_pedido(self, obj):
        return obj
    

    def _acertar_nota(self, obj):
        return obj


if __name__ == '__main__':
    app = TratamentoPlanilha(
        local_planilha='despachar_pedidos\pedidos_x_notas.xlsx',
        nome_aba_pedido='Pedido',
        nome_aba_nf='Nota'
    )
    print(app.retorno_dicionario())
       