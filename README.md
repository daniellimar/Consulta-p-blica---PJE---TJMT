# Documentação do Script de Busca de Processos

## Introdução

Este script utiliza Python para monitorar o status de processos no sistema PJE (Processo Judicial Eletrônico) e
notificar sobre atualizações. Ele combina bibliotecas como `tkinter` para a interface gráfica, `selenium` para automação
web, e `plyer` para notificações.

## Funcionalidades

- **Interface Gráfica**: Permite ao usuário inserir o número do processo, a URL do PJE e o intervalo de busca.
- **Busca Automática**: Utiliza `selenium` para acessar o site do PJE, inserir o número do processo e extrair a última
  movimentação.
- **Notificações**: Envia notificações com a última movimentação encontrada.
- **Atualização em Tempo Real**: Atualiza a interface gráfica com a última movimentação e a hora da consulta.

## Código

O script é composto pelas seguintes partes principais:

### Importação de Bibliotecas

### Funções

#### `enviar_notificacao(ultima_movimentacao)`

Envia uma notificação com a última movimentação do processo.

#### `atualizar_movimentacao(ultima_movimentacao, hora_consulta, label_movimentacao, label_hora)`

Atualiza as labels na interface gráfica com a última movimentação e a hora da consulta.

#### `buscar_status(numero_processo, url_pje, intervalo, label_movimentacao, label_hora)`

Função principal que busca o status do processo no PJE e atualiza a interface.

#### `iniciar_processamento()`

Inicia a busca do status do processo em uma thread separada.

### Interface Gráfica

A interface é criada com `tkinter` e inclui campos para inserir o número do processo, a URL do PJE e o intervalo de
busca.

## Uso

1. **Instalar Dependências**: Certifique-se de ter `tkinter`, `selenium`, `plyer`, e `webdriver` (como o ChromeDriver)
   instalados.
2. **Executar o Script**: Execute o script Python.
3. **Inserir Dados**: Insira o número do processo, a URL do PJE e o intervalo de busca na interface gráfica.
4. **Iniciar Busca**: Clique no botão "Iniciar" para começar a monitorar o processo.

## Considerações

- **Privacidade e Segurança**: Tenha cuidado ao inserir informações sensíveis.
- **Dependências**: Certifique-se de que todas as dependências estão atualizadas.
- **Compatibilidade**: Verifique se o script funciona corretamente com diferentes versões do navegador e do PJE.