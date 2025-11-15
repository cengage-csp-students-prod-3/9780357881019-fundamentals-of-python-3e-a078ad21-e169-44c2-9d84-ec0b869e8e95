
def shift_left(bit_string):
    """Shift a bit string one place to the left, wrapping the leftmost bit to the right."""
    if len(bit_string) == 0:
        return bit_string
    return bit_string[1:] + bit_string[0]

def char_to_bit_string(char):
    """Convert a character to a 7-bit binary string, add 1 to ASCII value first."""
    ascii_value = ord(char) + 1  
    bit_string = format(ascii_value, '07b')  
    shifted = shift_left(bit_string)         
    return shifted

def encrypt_message(message):
    encrypted_bits = [char_to_bit_string(c) for c in message]
    return ' '.join(encrypted_bits)

def main():
    message = input("Enter a message: ")
    encrypted = encrypt_message(message)
    print(encrypted)

if __name__ == "__main__":
    main()
