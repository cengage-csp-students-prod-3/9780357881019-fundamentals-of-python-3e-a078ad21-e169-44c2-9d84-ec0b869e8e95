

def shift_right(bit_string):
    """Shift a bit string one place to the right, wrapping the rightmost bit to the left."""
    if len(bit_string) == 0:
        return bit_string
    return bit_string[-1] + bit_string[:-1]

def bit_string_to_char(bit_string):
    """Convert a shifted 7-bit string to the original character."""
    shifted_back = shift_right(bit_string)           
    ascii_value = int(shifted_back, 2) - 1          
    return chr(ascii_value)

def decrypt_message(encrypted):
    bit_strings = encrypted.split()                  
    chars = [bit_string_to_char(b) for b in bit_strings]
    return ''.join(chars)

def main():
    coded_text = input("Enter the coded text: ")
    decrypted = decrypt_message(coded_text)
    print(decrypted)

if __name__ == "__main__":
    main()
