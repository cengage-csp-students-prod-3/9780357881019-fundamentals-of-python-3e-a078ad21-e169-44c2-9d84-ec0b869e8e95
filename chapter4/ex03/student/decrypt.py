# decrypt_file.py
# Decrypts an entire text file encrypted with a Caesar cipher

def caesar_decrypt(text, step):
    decrypted = ""
    for char in text:
        decrypted += chr((ord(char) - step) % 256)  # tüm ASCII karakterleri kapsar
    return decrypted

def main():
    input_file = input("Enter the input file name: ")
    output_file = input("Enter the output file name: ")
    step = int(input("Enter the distance value: "))

    # Dosyayı oku
    with open(input_file, "r", encoding="utf-8") as f:
        content = f.read()

    # Şifre çöz
    decrypted_content = caesar_decrypt(content, step)

    # Çözülmüş içeriği yaz
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(decrypted_content)

    print("File decrypted successfully!")

if __name__ == "__main__":
    main()
