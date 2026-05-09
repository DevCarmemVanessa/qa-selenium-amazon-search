from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Edge()

driver.get("https://www.amazon.com.br")

espera = WebDriverWait(driver, 10)

barra_pesquisa = espera.until(EC.presence_of_element_located((By.ID, "twotabsearchtextbox")))

barra_pesquisa.send_keys("notebook gamer")

botao_busca = driver.find_element(By.ID, "nav-search-submit-button")

botao_busca.click()

if "notebook gamer" in driver.title:
    print("Teste passou!")
else:
    print("Teste falhou!")

input("Pesquisa realizada com sucesso!")

input("Pressione Enter Para fechar...")

driver.quit()
