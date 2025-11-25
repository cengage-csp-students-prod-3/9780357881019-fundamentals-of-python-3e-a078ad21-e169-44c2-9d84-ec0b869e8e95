# concordance.py

def main():
    filename = input("Enter the input file name: ")
    
    try:
        with open(filename, 'r') as file:
            text = file.read()
        
        # Split text into words
        words = text.split()
        
        # Count word frequencies
        freq = {}
        for word in words:
            if word in freq:
                freq[word] += 1
            else:
                freq[word] = 1
        
        # Print words alphabetically with their frequency
        for word in sorted(freq):
            print(f"{word} {freq[word]}")
    
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

if __name__ == "__main__":
    main()
