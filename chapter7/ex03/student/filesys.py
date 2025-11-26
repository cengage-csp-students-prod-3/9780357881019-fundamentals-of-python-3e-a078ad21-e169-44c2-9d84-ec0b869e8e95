import os

# --- Fonksiyonlar ---

def listCurrentDirectory():
    current_dir = os.getcwd()
    files = os.listdir(current_dir)
    print(f"Files in {current_dir}:")
    for file in files:
        print(file)

def moveUp():
    try:
        os.chdir("..")
        print(f"Moved up. Current directory: {os.getcwd()}")
    except Exception as e:
        print(f"Error: {e}")

def moveDown():
    folder = input("Enter the folder name to move down into: ")
    if os.path.isdir(folder):
        os.chdir(folder)
        print(f"Moved down. Current directory: {os.getcwd()}")
    else:
        print(f"Error: '{folder}' is not a directory.")

def countFiles():
    files = [f for f in os.listdir() if os.path.isfile(f)]
    print(f"Number of files in the directory: {len(files)}")

def directorySize():
    total_size = 0
    for f in os.listdir():
        if os.path.isfile(f):
            total_size += os.path.getsize(f)
    print(f"Size of the directory in bytes: {total_size}")

def searchFile():
    name = input("Enter the file name to search for: ")
    if os.path.exists(name):
        print(f"File '{name}' found!")
    else:
        print(f"File '{name}' not found.")

def viewFile():
    # Mevcut dizindeki dosyaları listele
    current_dir = os.getcwd()
    files = os.listdir(current_dir)
    print(f"Files in {current_dir}:")
    for file in files:
        print(file)

    # Kullanıcıdan dosya adı iste
    file_name = input("Enter a file name from these names: ")

    # Dosya açma ve hata yönetimi
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            content = f.read()
            print("\n" + content)
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist.")
    except IOError:
        print(f"Error: Cannot read the file '{file_name}'.")

# --- Ana Program ---

while True:
    print("\n1   List the current directory")
    print("2   Move up")
    print("3   Move down")
    print("4   Number of files in the directory")
    print("5   Size of the directory in bytes")
    print("6   Search for a file name")
    print("7   View the contents of a file")
    print("8   Quit the program")
    
    choice = input("Enter a number: ")

    if choice == "1":
        listCurrentDirectory()
    elif choice == "2":
        moveUp()
    elif choice == "3":
        moveDown()
    elif choice == "4":
        countFiles()
    elif choice == "5":
        directorySize()
    elif choice == "6":
        searchFile()
    elif choice == "7":
        viewFile()
    elif choice == "8":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
