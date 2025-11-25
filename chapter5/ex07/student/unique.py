# unique.py

def main():
    filename = input("Enter the input file name: ")
    
    try:
        with open(filename, 'r') as file:
            text = file.read()
        
        # Split text into words
        words = text.split()
        
        # Convert to a set to remove duplicates
        unique_words = set(words)
        
        # Sort alphabetically
        sorted_words = sorted(unique_words)
        
        # Print each word on a separate line
        for word in sorted_words:
            print(word)
    
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

if __name__ == "__main__":
    main()
