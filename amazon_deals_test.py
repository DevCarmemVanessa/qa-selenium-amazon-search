from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Edge()

driver.get("https://www.amazon.com.br/deals")

espera = WebDriverWait(driver, 10)

if "deals" in driver.current_url:
    print("Teste passou!")
else:
    print("Teste falhou!")

print(driver.title)
if "Ofertas" in driver.page_source:
    print("Elemento encontrado!")
else:
    print("Elemento não encontrado")

input("Pressione Enter para finalizar...")

driver.quit()
