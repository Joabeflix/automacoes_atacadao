import pyautogui
import os

imagens_salvar_print = ['M025D', 'M026B', 'M029L', 'W905', 'M029J', 'D669', 'W838']

os.system('cls')
print('')
for img in imagens_salvar_print:
    os.system('cls')
    confirmacao = input(f'Imagem atual: {img} press - [Enter]')
    screenshot = pyautogui.screenshot(region=(0, 0, 1920, 1080))

    nome_arquivo = f'{img}.jpg'
    screenshot.save(nome_arquivo)


