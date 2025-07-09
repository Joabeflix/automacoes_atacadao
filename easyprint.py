import pyautogui
import os
import pyperclip
import time

produtos = [
    "48430NAFL",
    "48420CV",
    "59922FF",
    "48619NA",
    "51525B"
]

os.system('cls')
print('')

pulados = []

for img in produtos:
    os.system('cls')
    pyperclip.copy(img)
    entrada = input(f'Imagem atual: {img} - Pressione [Enter] para ...')
    if entrada == 'p':
        pulados.append(img)
        continue

    
    
    print('MOVA O MOUSE PARA A POSIÇÂO SUPERIOR ESQUERDA')
    time.sleep(2)
    x1, y1 = pyautogui.position()
    print(f'X1: {x1}, Y1: {y1}')

    print('MOVA O MOUSE PARA A POSIÇÂO INFERIOR DIREITA')
    time.sleep(2.2)
    x2, y2 = pyautogui.position()
    print(f'X2: {x2}, Y2: {y2}')

    region = (x1, y1, x2 - x1, y2 - y1)


    screenshot = pyautogui.screenshot(region=region)

    nome_arquivo = f'{img}.jpg'
    screenshot.save(nome_arquivo)
    print(f'[✓] Imagem salva como {nome_arquivo}')


if pulados:
    print('PULADOS: ')
    for p in pulados:
        print(p)

