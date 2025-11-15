

def shift_right(bit_string):
    if len(bit_string) == 0:
        return bit_string
    # sağ bit string[-1], kalan string[:-1]
    return bit_string[-1] + bit_string[:-1]

def main():
    bits = input("Enter a string of bits: ")
    shifted = shift_right(bits)
    print(shifted)

if __name__ == "__main__":
    main()
