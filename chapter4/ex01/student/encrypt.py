# encrypt.py
# Caesar cipher for ALL printable ASCII characters (32..126).
# Prompts:
#   Enter a message: 
#   Enter the distance value: 
# If the distance is not an integer, prints a friendly error and exits.

def main():
    plaintext = input("Enter a message: ")
    dist_str = input("Enter the distance value: ")

    # Validate distance is an integer
    try:
        distance = int(dist_str)
    except ValueError:
        print("Error: distance value must be an integer.")
        return

    # Printable ASCII range: 32..126 inclusive (95 characters)
    MIN_PRINT = 32
    MAX_PRINT = 126
    RANGE = MAX_PRINT - MIN_PRINT + 1  # 95

    # Normalize distance so it's within 0..RANGE-1
    distance = distance % RANGE

    encrypted_chars = []
    for ch in plaintext:
        code = ord(ch)
        if MIN_PRINT <= code <= MAX_PRINT:
            # shift within printable range
            offset = code - MIN_PRINT
            new_offset = (offset + distance) % RANGE
            new_code = MIN_PRINT + new_offset
            encrypted_chars.append(chr(new_code))
        else:
            # If character is outside printable range (rare for input), leave as is
            encrypted_chars.append(ch)

    encrypted = "".join(encrypted_chars)
    print(encrypted)

if __name__ == "__main__":
    main()

