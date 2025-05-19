from selenium import webdriver
from selenium.webdriver.common.by import By
import pickle
import time
import winsound

driver = webdriver.Chrome()

driver.get("https://www.mercadolivre.com.br/")
time.sleep(3)

with open("cookies.pkl", "rb") as f:
    cookies = pickle.load(f)

for cookie in cookies:
    driver.add_cookie(cookie)

driver.get("https://www.mercadolivre.com.br/resumo#menu-user")
time.sleep(5)

while True:
    lista_dados = [] 
    try:
        driver.refresh()
        time.sleep(3)

        elementos = driver.find_elements(By.CLASS_NAME, "andes-card__content")

        print("==== Conteúdo capturado ====")
        for el in elementos:
            texto = el.text.strip()
            if texto:
                lista_dados.append(texto)
                print(texto)
        print("============================\n")
        
    except Exception as e:
        print("Erro ao capturar o texto:", str(e))

    if 'Não há perguntas a responder.' not in lista_dados:
        winsound.Beep(500, 5000)

    time.sleep(300)
