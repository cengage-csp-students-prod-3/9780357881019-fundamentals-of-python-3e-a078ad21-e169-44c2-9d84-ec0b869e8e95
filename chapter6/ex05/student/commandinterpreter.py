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
    menu = ["Open", "Save", "Compile", "Run", "Quit"]

    while True:
        printMenu(menu)
        command = acceptCommand(len(menu))
        performCommand(command, menu)

        if menu[command - 1] == "Quit":
            print("Have a nice day!")
            break


if __name__ == "__main__":
    main()
