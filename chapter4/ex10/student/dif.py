# dif.py
# Compares two text files line by line

def main():
    file1_name = input("Enter the first file name: ")
    file2_name = input("Enter the second file name: ")

    with open(file1_name, "r", encoding="utf-8") as f1, \
         open(file2_name, "r", encoding="utf-8") as f2:

        same = True
        while True:
            line1 = f1.readline()
            line2 = f2.readline()

            # Her iki dosya da sona geldiyse döngüden çık
            if not line1 and not line2:
                break

            # Satırlar farklıysa veya bir dosya bitti diğer bitmedi
            if line1 != line2:
                same = False
                print("No")
                # Sona gelmiş ama diğer dosya devam ediyorsa boş string yerine newline önle
                print(line1.rstrip("\n"))
                print(line2.rstrip("\n"))
                break

        if same:
            print("Yes")

if __name__ == "__main__":
    main()

