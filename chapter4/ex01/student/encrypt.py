# encrypt.py
# This program encrypts a message using a Caesar cipher for all printable characters.

def main():
    # Get input from the user
    plaintext = input("Enter a message: ")
    distance = int(input("Enter the distance value: "))

    encrypted = ""

    # Encrypt each character
    for ch in plaintext:
        # Convert the character to its ASCII code, shift it, and wrap around the printable range
        new_code = (ord(ch) + distance) % 127  # 127 is outside printable range
        if new_code < 32:  # printable characters start from 32 (space)
            new_code += 32
        encrypted += chr(new_code)

    # Print encrypted message
    print(encrypted)

if __name__ == "__main__":
    main()

