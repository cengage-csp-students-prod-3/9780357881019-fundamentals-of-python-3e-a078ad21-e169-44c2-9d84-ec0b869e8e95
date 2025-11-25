# concordance.py

def main():
    filename = input("Enter the input file name: ")
    
    try:
        with open(filename, 'r') as file:
            text = file.read()
        
        # Split text into words
        words = text.split()
        
        # Dictionary to store word frequencies
        freq = {}
        for word in words:
            word_lower = word.lower()  # Optional: make it case-insensitive
            if word_lower in freq:
                freq[word_lower] += 1
            else:
                freq[word_lower] = 1
        
        # Sort words alphabetically
        for word in sorted(freq):
            print(f"{word} {freq[word]}")
    
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

if __name__ == "__main__":
    main()

