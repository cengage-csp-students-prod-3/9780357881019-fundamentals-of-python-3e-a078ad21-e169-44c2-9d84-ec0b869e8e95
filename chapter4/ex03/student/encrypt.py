
def caesar_encrypt(text, step):
    encrypted = ""
    for char in text:
        encrypted += chr((ord(char) + step) % 256)  
    return encrypted

def main():
    input_file = input("Enter the input file name: ")
    output_file = input("Enter the output file name: ")
    step = int(input("Enter the distance value: "))

   
    with open(input_file, "r", encoding="utf-8") as f:
        content = f.read()

    
    encrypted_content = caesar_encrypt(content, step)

  
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(encrypted_content)

    print("File encrypted successfully!")

if __name__ == "__main__":
    main()
