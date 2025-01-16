import os
import pyaes

def decrypt_files_in_directory():
    # Mensagem para o novo arquivo leia-me.txt
    ransom_message = "voce foi um bom garoto hehe"

    # Chave de criptografia (deve ser a mesma usada para criptografar)
    key = b"testeransomwares"

    # Lista de arquivos no diretório atual com a extensão .ransomwaretroll
    files = [f for f in os.listdir('.') if f.endswith('.ransomwaretroll')]

    for file_name in files:
        try:
            # Abrir o arquivo criptografado para leitura em modo binário
            with open(file_name, "rb") as file:
                crypto_data = file.read()

            # Descriptografar o conteúdo do arquivo
            aes = pyaes.AESModeOfOperationCTR(key)
            original_data = aes.decrypt(crypto_data)

            # Restaurar o nome original do arquivo (remover a extensão .ransomwaretroll)
            original_file_name = file_name.replace(".ransomwaretroll", "")
            with open(original_file_name, "wb") as original_file:
                original_file.write(original_data)

            # Remover o arquivo criptografado
            os.remove(file_name)

            print(f"Arquivo {file_name} restaurado com sucesso para {original_file_name}.")
        except Exception as e:
            print(f"Erro ao processar o arquivo {file_name}: {e}")

    # Remover o arquivo leia-me.txt se existir
    if os.path.exists("leia-me.txt"):
        os.remove("leia-me.txt")
        print("Arquivo leia-me.txt removido.")

    # Criar o arquivo leia-me-de-novo.txt com a nova mensagem
    with open("leia-me-de-novo.txt", "w") as ransom_file:
        ransom_file.write(ransom_message)

    print("Processo concluído. Arquivo leia-me-de-novo.txt criado.")

if __name__ == "__main__":
    decrypt_files_in_directory()
