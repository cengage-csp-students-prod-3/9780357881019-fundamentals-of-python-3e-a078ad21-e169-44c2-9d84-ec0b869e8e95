
def shift_left(bit_string):
    if len(bit_string) == 0:
        return bit_string
    # sol bit string[0], kalan string[1:]
    return bit_string[1:] + bit_string[0]

def main():
    bits = input("Enter a string of bits: ")
    shifted = shift_left(bits)
    print(shifted)

if __name__ == "__main__":
    main()
