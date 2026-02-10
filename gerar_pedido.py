import pyautogui
import time
import pandas as pd
import pyautogui
import time

def verificar_erro_totvs(timeout=0.8):
    """
    Retorna:
    - False → se erro foi detectado (após pausa manual)
    - True  → se nenhum erro apareceu
    """
    inicio = time.time()

    while time.time() - inicio < timeout:
        try:
            botao = pyautogui.locateCenterOnScreen(
                'botao_erro.png',
                confidence=0.8
            )

            if botao:
                pyautogui.click(botao)
                time.sleep(0.5)

                print("\n⚠️ ERRO DETECTADO NO TOTVS")
                print("Resolva o problema na tela.")
                input("👉 Pressione ENTER para continuar...")
                time.sleep(4)
                return False  # ERRO DETECTADO
        

        except pyautogui.ImageNotFoundException:
            pass

    return True  # NENHUM ERRO




def print_comando(x):
    print(f'---> Comando: [{x}]')

def fazer_pedido(sku, qtd):
    print_comando('Direita')
    pyautogui.press('right', presses=1, interval=0.1)
    time.sleep(1)
    print_comando(f'Escrevendo [{sku}]')
    pyautogui.write(str(sku), interval=0.05)
    # print('Sku inserido com sucesso')
    time.sleep(0.7)
    print_comando('Tab')
    pyautogui.press('tab')
    time.sleep(1)
    print_comando('Direita')
    pyautogui.press('right', presses=1, interval=0.1)
    time.sleep(0.3)
    print_comando('Direita')
    pyautogui.press('right', presses=1, interval=0.1)

    time.sleep(0.2)
    print_comando(f'Escrevendo [{qtd}]')
    pyautogui.write(str(qtd), interval=0.3)
    time.sleep(2)

    print_comando('Enter')
    pyautogui.press('enter', presses=1, interval=0.1)
    if verificar_erro_totvs():
        time.sleep(0.9)
        print_comando('Baixo')
        pyautogui.press('down', presses=1, interval=0.1)
        time.sleep(1.8)
    
    
local = rf'C:\Users\joab.alves\Downloads\05 PARTE M48 P 50.xlsx'
planilha = pd.read_excel(local, sheet_name='pedido')

coluna_sku = planilha['SKU']
coluna_qtd = planilha['QTD']
time.sleep(5)
for sku, qtd in zip(coluna_sku, coluna_qtd):
    # input('Clique [Ok] para fazer com o próximo...')
    print('Colocando ítem no pedido...')
    print(f'SKU: {sku}\nQTD: {qtd}')
    fazer_pedido(sku, qtd)
    print('Produto inserido com sucesso.')
    print(f'{'-' * 50}')






