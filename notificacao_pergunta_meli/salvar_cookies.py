from selenium import webdriver
import time
import pickle  # Para salvar os cookies

# Abre o navegador
driver = webdriver.Chrome()

# Vai para o Mercado Livre
driver.get("https://www.mercadolivre.com.br/")

# Aguarda login manual
print("Faça o login manualmente...")
input("Pressione Enter depois de logar...")

# Salva os cookies em um arquivo
with open("cookies.pkl", "wb") as f:
    pickle.dump(driver.get_cookies(), f)

print("Cookies salvos com sucesso.")
driver.quit()
