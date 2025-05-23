from selenium import webdriver 
from selenium.webdriver.common.by import By
import pickle
import time
import pygame
import random
import pyautogui
import winsound


# Inicializa o mixer de áudio
pygame.mixer.init()

# Mapeia os áudios com base no número sorteado
audios = {
    1: "joabe-caio.mp3",
    2: "keyton-caio.mp3"
}

driver = webdriver.Chrome()

driver.get("https://www.mercadolivre.com.br/")
time.sleep(3)

with open("cookies.pkl", "rb") as f:
    cookies = pickle.load(f)

for cookie in cookies:
    driver.add_cookie(cookie)

driver.get("https://www.mercadolivre.com.br/resumo#menu-user")

time.sleep(5)

largura, altura = pyautogui.size()

# Define a posição no canto direito, meio vertical
x = largura - 100     # 10px da borda direita
y = altura // 2      # Meio da altura

pyautogui.click(x, y)

time.sleep(5)

while True:
    lista_dados = [] 
    try:
        driver.refresh()
        time.sleep(3)

        elementos = driver.find_elements(By.CLASS_NAME, "andes-card__content")

        for el in elementos:
            texto = el.text.strip()
            if texto:
                lista_dados.append(texto)
        
    except Exception as e:
        print("Erro ao capturar o texto:", str(e))

    if 'Não foi possível mostrar as perguntas.' in lista_dados:
        continue

    if 'Não há perguntas a responder.' not in lista_dados:

        for v in range(12):
            winsound.Beep(500, 200)
            winsound.Beep(1000, 100)
            winsound.Beep(2000, 50)

        time.sleep(1.5)
        """"""
        numero = random.randint(1, 2)
        audio_sorteado = audios[numero]
        print(f"[INFO] Nova pergunta detectada — tocando áudio {numero}: {audio_sorteado}")
        
        pygame.mixer.music.load(audio_sorteado)
        pygame.mixer.music.play()

        # Espera o áudio terminar
        while pygame.mixer.music.get_busy():
            time.sleep(1)

    for x in range(200):
        print(x)
        time.sleep(1)
