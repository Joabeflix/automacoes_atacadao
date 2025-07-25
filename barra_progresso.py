import time
import os

def simulacao(qtd, obj_barra):
    for x in range(qtd):
        obj_barra.atualizar_barra()
    obj_barra.fim_barra()

class BarraProgresso:
    def __init__(self, idc, texto=None):
        self.idc=idc
        self.porcentagem = 0
        self.texto=texto

    def atualizar_barra(self):
        os.system('cls')
        print(f'[{str('X' * int(self.porcentagem))}{'_' * (100-int(self.porcentagem))}]' )
        print(f'[{int(self.porcentagem)}%]'.center(100, ' '))
        if self.texto:
            print(self.texto)
        self.porcentagem+=(100 / self.idc)

    def fim_barra(self):
        os.system('cls')
        print(f"[{"X" * 100}]")
        print(f"[100 %]".center(100, ' '))
        if self.texto:
            print(self.texto)

simular = 100

br = BarraProgresso(idc=simular)
simulacao(simular, br)








