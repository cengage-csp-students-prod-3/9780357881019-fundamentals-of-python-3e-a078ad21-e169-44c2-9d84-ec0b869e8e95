def main():
    # Ask the user for the filename
    filename = input("Enter the input file name: ")

    try:
        with open(filename, 'r') as file:
            # Read all numbers as a single string and split into list
            numbers_str = file.read().split()
            
            # Convert strings to integers using map (higher-order function)
            numbers = list(map(int, numbers_str))
            
            # Compute average using sum and len (sum is a higher-order function)
            if numbers:
                avg = sum(numbers) / len(numbers)
                print(f"The average is {avg}")
            else:
                print("The file is empty. No numbers to average.")
    
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except ValueError:
        print("Error: The file contains non-numeric data.")

# Run the program
if __name__ == "__main__":
    main()
