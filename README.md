# Descrição do Projeto

Este repositório contém scripts em Python que realizam a criptografia e descriptografia de arquivos de texto (`.txt`) no diretório atual. Os scripts foram desenvolvidos como parte de um estudo oferecido pela **Santander Academy** e pela **DIO (Digital Innovation One)**.

## Funcionalidades

### 1. Criptografia de Arquivos
O primeiro script realiza as seguintes ações:
- Identifica todos os arquivos `.txt` no diretório atual, excluindo arquivos específicos como `leia-me.txt`.
- Criptografa os conteúdos dos arquivos usando o algoritmo AES no modo CTR, com uma chave fixa.
- Salva os arquivos criptografados com a extensão `.ransomwaretroll`.
- Remove os arquivos originais após a criptografia.
- Cria um arquivo chamado `leia-me.txt` contendo a mensagem "voce foi atacado hahaha".

### 2. Descriptografia de Arquivos
O segundo script reverte as ações do script de criptografia, realizando as seguintes etapas:
- Identifica todos os arquivos com a extensão `.ransomwaretroll` no diretório atual.
- Descriptografa os conteúdos dos arquivos usando a mesma chave AES utilizada no processo de criptografia.
- Restaura os arquivos com seus nomes originais (removendo a extensão `.ransomwaretroll`).
- Remove os arquivos criptografados após a restauração.
- Exclui o arquivo `leia-me.txt`, caso exista.
- Cria um novo arquivo chamado `leia-me-de-novo.txt` com a mensagem "voce foi um bom garoto hehe".

## Como Usar

### Pré-requisitos
- Python 3 instalado no sistema.
- Biblioteca `pyaes` instalada. Caso não esteja instalada, utilize o comando abaixo para instalá-la:
  ```bash
  pip install pyaes

---

## 🚨 **Aviso Importante**

Este projeto é exclusivamente para fins educacionais. **NÃO** utilize este código para atividades maliciosas ou ilegais. O uso inadequado deste código é estritamente proibido e pode acarretar em penalidades legais severas.

---

