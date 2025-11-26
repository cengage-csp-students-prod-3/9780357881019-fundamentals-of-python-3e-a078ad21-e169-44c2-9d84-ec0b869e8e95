import os

def displayFiles(pathname):
    """
    Recursively display file names and their contents.
    If pathname is a directory, apply the function to each item in it.
    """
    if os.path.isfile(pathname):
        # If it is a file, print its name and contents
        print(f"File name: {pathname}")
        with open(pathname, 'r') as file:
            contents = file.read()
            print(contents)
    elif os.path.isdir(pathname):
        # If it is a directory, print the directory name
        print(f"Directory name: {pathname}")
        # Recursively call displayFiles on each item in the directory
        for item in os.listdir(pathname):
            item_path = os.path.join(pathname, item)
            displayFiles(item_path)
    else:
        print(f"{pathname} is not a valid file or directory.")

# Test the function
if __name__ == "__main__":
    directory = input("Directory name: ")
    displayFiles(directory)
