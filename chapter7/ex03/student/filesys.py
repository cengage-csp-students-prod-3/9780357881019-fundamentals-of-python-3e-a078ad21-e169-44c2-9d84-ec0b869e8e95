"""
Program: filesys.py
Author: Ken

Provides a menu-driven tool for navigating a file system
and gathering information on files.
"""

import os

QUIT = '8'
COMMANDS = tuple(str(i) for i in range(1, 9))

MENU = """1   List the current directory
2   Move up
3   Move down
4   Number of files in the directory
5   Size of the directory in bytes
6   Search for a file name
7   View the contents of a file
8   Quit the program"""

def main():
    while True:
        print(os.getcwd())
        print(MENU)
        command = acceptCommand()
        runCommand(command)
        if command == QUIT:
            print("Have a nice day!")
            break

def acceptCommand():
    while True:
        command = input("Enter a number: ")
        if command not in COMMANDS:
            print("Error: command not recognized")
        else:
            return command

def runCommand(command):
    if command == '1':
        listCurrentDir(os.getcwd())
    elif command == '2':
        moveUp()
    elif command == '3':
        moveDown()
    elif command == '4':
        print("The total number of files is", countFiles(os.getcwd()))
    elif command == '5':
        print("The total number of bytes is", countBytes(os.getcwd()))
    elif command == '6':
        target = input("Enter the search string: ")
        fileList = findFiles(target, os.getcwd())
        if not fileList:
            print("String not found")
        else:
            for f in fileList:
                print(f)
    elif command == '7':
        viewFile()

def listCurrentDir(dirName):
    for element in os.listdir(dirName):
        print(element)

def moveUp():
    os.chdir("..")

def moveDown():
    newDir = input("Enter the directory name: ")
    if os.path.exists(os.path.join(os.getcwd(), newDir)) and os.path.isdir(newDir):
        os.chdir(newDir)
    else:
        print("ERROR: no such name")

def countFiles(path):
    count = 0
    for element in os.listdir(path):
        fullPath = os.path.join(path, element)
        if os.path.isfile(fullPath):
            count += 1
        elif os.path.isdir(fullPath):
            count += countFiles(fullPath)
    return count

def countBytes(path):
    count = 0
    for element in os.listdir(path):
        fullPath = os.path.join(path, element)
        if os.path.isfile(fullPath):
            count += os.path.getsize(fullPath)
        elif os.path.isdir(fullPath):
            count += countBytes(fullPath)
    return count

def findFiles(target, path):
    files = []
    for element in os.listdir(path):
        fullPath = os.path.join(path, element)
        if os.path.isfile(fullPath):
            if target in element:
                files.append(fullPath)
        elif os.path.isdir(fullPath):
            files.extend(findFiles(target, fullPath))
    return files

def viewFile():
    print("Files in", os.getcwd() + ":")
    files = [f for f in os.listdir(os.getcwd()) if os.path.isfile(f)]
    for f in files:
        print(f)
    filename = input("Enter a file name from these names: ")
    filepath = os.path.join(os.getcwd(), filename)
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            print(f.read())
    except FileNotFoundError:
        print("Error: file not found")

if __name__ == "__main__":
    main()
