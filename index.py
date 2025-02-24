from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Configurar o driver (certifique-se de ter o ChromeDriver instalado)
driver = webdriver.Chrome()

try:
    # Abrir a página do PJE
    driver.get("https://pje.tjmt.jus.br/pje/ConsultaPublica/listView.seam")
    time.sleep(5)  # Esperar a página carregar completamente

    # Localizar o campo de entrada do número do processo
    campo_processo = driver.find_element(By.ID,
                                         "fPP:numProcesso-inputNumeroProcessoDecoration:numProcesso-inputNumeroProcesso")

    # Inserir o número do processo
    numero_processo = "numero_processo"
    campo_processo.send_keys(numero_processo)

    # Pressionar Enter para pesquisar
    campo_processo.send_keys(Keys.RETURN)

    # Aguardar o carregamento da página
    time.sleep(5)

    # Localizar a primeira linha da tabela na coluna "Última movimentação"
    ultima_movimentacao = driver.find_element(By.XPATH, "//table[@id='fPP:processosTable']//tbody//tr[1]//td[3]").text

    print(f"Última Movimentação: {ultima_movimentacao}")

finally:
    # Fechar o navegador
    driver.quit()
