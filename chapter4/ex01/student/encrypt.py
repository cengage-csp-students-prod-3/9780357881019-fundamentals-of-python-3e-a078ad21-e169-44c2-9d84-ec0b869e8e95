# encrypt.py
# Caesar cipher shifting all ASCII characters (0..127)

def main():
    plaintext = input("Enter a message: ")
    dist_str = input("Enter the distance value: ")

    try:
        distance = int(dist_str)
    except ValueError:
        
        distance = sum(ord(c) for c in dist_str) % 128

    encrypted = ""

    for ch in plaintext:
        new_code = (ord(ch) + distance) % 128
        encrypted += chr(new_code)

    print(encrypted)

if __name__ == "__main__":
    main()
