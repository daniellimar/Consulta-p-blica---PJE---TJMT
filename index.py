from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from plyer import notification


def enviar_notificacao(ultima_movimentacao):
    notification.notify(
        title="Última Movimentação do Processo",
        message=f"A última movimentação do processo é: {ultima_movimentacao}",
        timeout=10
    )


def buscar_status():
    while True:
        driver = webdriver.Chrome()

        try:
            # Abrir a página do PJE
            driver.get("https://pje.tjmt.jus.br/pje/ConsultaPublica/listView.seam")
            time.sleep(5)

            # Localizar o campo de entrada do número do processo
            campo_processo = driver.find_element(By.ID,
                                                 "fPP:numProcesso-inputNumeroProcessoDecoration:numProcesso-inputNumeroProcesso")

            # Inserir o número do processo
            numero_processo = "1006449-94.2025.8.11.0002"
            campo_processo.send_keys(numero_processo)

            # Pressionar Enter para pesquisar
            campo_processo.send_keys(Keys.RETURN)

            # Aguardar o carregamento da página
            time.sleep(5)

            # Localizar a primeira linha da tabela na coluna "Última movimentação"
            ultima_movimentacao = driver.find_element(By.XPATH,
                                                      "//table[@id='fPP:processosTable']//tbody//tr[1]//td[3]").text

            print(f"Última Movimentação: {ultima_movimentacao}")

            enviar_notificacao(ultima_movimentacao)

        finally:
            driver.quit()

        time.sleep(5)


if __name__ == "__main__":
    buscar_status()
