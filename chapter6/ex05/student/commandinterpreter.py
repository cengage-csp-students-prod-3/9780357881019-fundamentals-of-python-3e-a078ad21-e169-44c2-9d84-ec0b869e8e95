# commandinterpreter.py

def printMenu(menu):
    for i in range(len(menu)):
        print(f"{i + 1} {menu[i]}")


def acceptCommand(menuLength):
    while True:
        try:
            choice = int(input("Enter a number: "))
            if 1 <= choice <= menuLength:
                return choice
            else:
                print("Error: invalid number.")
        except ValueError:
            print("Error: please enter a number.")


def performCommand(commandNumber, menu):
    print(f"Command = {menu[commandNumber - 1]}")


def main():
    menu1 = ["Open", "Save", "Compile", "Run", "Quit"]

    while True:
        printMenu(menu1)
        command = acceptCommand(len(menu1))
        performCommand(command, menu1)

        if menu1[command - 1] == "Quit":
            print("Have a nice day!")
            break

    # Program ikinci menü ile test edilebilir:
    print("\nTesting with second menu...\n")
    menu2 = ["Login", "Upload", "Download", "Logout", "Quit"]

    while True:
        printMenu(menu2)
        command = acceptCommand(len(menu2))
        performCommand(command, menu2)

        if menu2[command - 1] == "Quit":
            print("Have a nice day!")
            break


if __name__ == "__main__":
    main()
