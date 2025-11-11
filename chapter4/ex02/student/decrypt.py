# decrypt.py
# This program decrypts a message that was encrypted using a Caesar cipher.
# It works for all ASCII characters (0..127).

def main():
    # Get input from the user
    coded_text = input("Enter the coded text: ")
    dist_str = input("Enter the distance value: ")

    try:
        distance = int(dist_str)
    except ValueError:
        # Fallback if input is not an integer
        distance = sum(ord(c) for c in dist_str) % 128

    plaintext = ""

    for ch in coded_text:
        # Reverse the Caesar shift
        new_code = (ord(ch) - distance) % 128
        plaintext += chr(new_code)

    print(plaintext)

if __name__ == "__main__":
    main()
