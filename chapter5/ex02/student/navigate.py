# navigate.py

def main():
    # Prompt the user for the filename
    filename = input("Enter the input file name: ")
    
    try:
        # Read all lines of the file into a list
        with open(filename, 'r') as file:
            lines = file.readlines()
            
        # Strip newline characters from each line
        lines = [line.rstrip('\n') for line in lines]
        
        while True:
            # Show the number of lines
            print(f"The file has {len(lines)} lines.")
            
            # Prompt for a line number
            num = int(input("Enter a line number [0 to quit]: "))
            
            if num == 0:
                break  # Quit the loop
            elif 1 <= num <= len(lines):
                print(f"{num} : {lines[num - 1]}")
            else:
                print("Invalid line number. Try again.")
    
    except FileNotFoundError:
        print("File not found. Please check the filename and try again.")

# Entry point for the program
if __name__ == "__main__":
    main()
