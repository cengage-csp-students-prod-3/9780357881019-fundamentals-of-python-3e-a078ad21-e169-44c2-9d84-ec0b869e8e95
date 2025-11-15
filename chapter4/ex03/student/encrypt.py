# encrypt_file.py
# Encrypts an entire text file using a Caesar cipher

def caesar_encrypt(text, step):
    encrypted = ""
    for char in text:
        encrypted += chr((ord(char) + step) % 256)  # tüm ASCII karakterleri kapsar
    return encrypted

def main():
    input_file = input("Enter the input file name: ")
    output_file = input("Enter the output file name: ")
    step = int(input("Enter the distance value: "))

    # Dosyayı oku
    with open(input_file, "r", encoding="utf-8") as f:
        content = f.read()

    # Şifrele
    encrypted_content = caesar_encrypt(content, step)

    # Şifrelenmiş içeriği yaz
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(encrypted_content)

    print("File encrypted successfully!")

if __name__ == "__main__":
    main()
