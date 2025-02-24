import tkinter as tk
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from plyer import notification
from datetime import datetime


def enviar_notificacao(ultima_movimentacao):
    notification.notify(
        title="Última Movimentação do Processo",
        message=f"A última movimentação do processo é: {ultima_movimentacao}",
        timeout=10
    )


def atualizar_movimentacao(ultima_movimentacao, hora_consulta, label_movimentacao, label_hora):
    label_movimentacao.config(text=f"Última Movimentação: {ultima_movimentacao}")
    label_hora.config(text=f"Hora da Consulta: {hora_consulta}")
    label_movimentacao.update_idletasks()
    label_hora.update_idletasks()


def buscar_status(numero_processo, url_pje, intervalo, label_movimentacao, label_hora):
    while True:
        driver = webdriver.Chrome()

        try:
            driver.get(url_pje)
            time.sleep(5)  # Esperar a página carregar completamente

            # Localizar o campo de entrada do número do processo
            campo_processo = driver.find_element(By.ID,
                                                 "fPP:numProcesso-inputNumeroProcessoDecoration:numProcesso-inputNumeroProcesso")

            # Inserir o número do processo
            campo_processo.send_keys(numero_processo)

            # Pressionar Enter para pesquisar
            campo_processo.send_keys(Keys.RETURN)

            # Aguardar o carregamento da página
            time.sleep(5)

            # Localizar a primeira linha da tabela na coluna "Última movimentação"
            ultima_movimentacao = driver.find_element(By.XPATH,
                                                      "//table[@id='fPP:processosTable']//tbody//tr[1]//td[3]").text

            print(f"Última Movimentação:")
            print({ultima_movimentacao})

            hora_consulta = datetime.now().strftime("%H:%M:%S")

            enviar_notificacao(ultima_movimentacao)

            atualizar_movimentacao(ultima_movimentacao, hora_consulta, label_movimentacao, label_hora)

        finally:
            driver.quit()

        time.sleep(intervalo * 60)


def iniciar_processamento():
    numero_processo = numero_processo_entry.get()
    url_pje = url_entry.get()
    intervalo = int(intervalo_entry.get())

    import threading
    threading.Thread(target=buscar_status, args=(numero_processo, url_pje, intervalo, label_movimentacao, label_hora),
                     daemon=True).start()


root = tk.Tk()
root.title("Busca de Processos")

root.geometry("400x350")

tk.Label(root, text="Número do Processo:").pack(pady=5)
numero_processo_entry = tk.Entry(root, width=30)
numero_processo_entry.insert(0, "numero_processo_entry")
numero_processo_entry.pack(pady=5)

tk.Label(root, text="URL do PJE:").pack(pady=5)
url_entry = tk.Entry(root, width=30)
url_entry.insert(0, "https://pje.tjmt.jus.br/pje/ConsultaPublica/listView.seam")
url_entry.pack(pady=5)

tk.Label(root, text="Intervalo (minutos):").pack(pady=5)
intervalo_entry = tk.Entry(root, width=30)
intervalo_entry.insert(0, "30")
intervalo_entry.pack(pady=5)

label_movimentacao = tk.Label(root, text="Última Movimentação: Nenhuma", width=50, height=2)
label_movimentacao.pack(pady=10)

label_hora = tk.Label(root, text="Hora da Consulta: Nenhuma", width=50, height=2)
label_hora.pack(pady=10)

iniciar_button = tk.Button(root, text="Iniciar", command=iniciar_processamento)
iniciar_button.pack(pady=20)

root.mainloop()
