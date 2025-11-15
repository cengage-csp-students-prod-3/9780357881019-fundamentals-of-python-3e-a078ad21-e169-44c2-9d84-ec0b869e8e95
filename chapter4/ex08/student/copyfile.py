# copyfile.py
# Copies the contents of one text file to another

def main():
    input_file = input("Enter the input file name: ")
    output_file = input("Enter the output file name: ")

    # Girdi dosyasını oku
    with open(input_file, "r", encoding="utf-8") as f:
        content = f.read()

    # Çıktı dosyasına yaz
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(content)

    print("File copied successfully!")

if __name__ == "__main__":
    main()
