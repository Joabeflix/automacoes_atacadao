import pandas as pd
from utils.utils import texto_no_console



class TratamentoPlanilhaMercadoLivre:
    def __init__(self, local_planilha, nome_aba_cod_rastreiro, nome_aba_nome_cliente):
        self.local_planilha = local_planilha
        self.nome_aba_cod_rastreiro = nome_aba_cod_rastreiro
        self.nome_aba_nome_cliente = nome_aba_nome_cliente

        try:
            planilha = pd.read_excel(self.local_planilha, header=5)
            self.lista_cod_rastreio, self.lista_nome_cliente = list(planilha[self.nome_aba_cod_rastreiro]), list(planilha[self.nome_aba_nome_cliente])

   
        except FileNotFoundError:
            texto_no_console('Erro ao ler a planilha. O arquivo não foi encontrado. Verifique o local do arquivo.')
            return None
        


    def _criar_dicionario(self):
        
        dicionario = {}

        for cod_rastreio, nome_cliente in zip(self.lista_cod_rastreio, self.lista_nome_cliente):
            if cod_rastreio == ' ':
                continue
            dicionario[self._acertar_codigo(cod_rastreio)] = {'nome_cliente': nome_cliente, 'status_conferencia': False}
 
        return dicionario
    
    def _acertar_codigo(self, codigo):
        return codigo[3:14]
    



if __name__ == "__main__":
    app = TratamentoPlanilhaMercadoLivre(
        local_planilha=rf'C:\Users\joabe\Desktop\dados_meli.xlsx',
        nome_aba_cod_rastreiro='Número de rastreamento',
        nome_aba_nome_cliente='Dados pessoais ou da empresa'
    )
    print(app._criar_dicionario())
        
            

