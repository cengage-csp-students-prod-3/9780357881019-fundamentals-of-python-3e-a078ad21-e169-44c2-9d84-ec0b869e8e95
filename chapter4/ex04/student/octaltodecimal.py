# octaltodecimal.py
# Converts a string of octal digits to decimal

def octal_to_decimal(octal_string):
    decimal_value = 0
    power = len(octal_string) - 1
    for digit in octal_string:
        decimal_value += int(digit) * (8 ** power)
        power -= 1
    return decimal_value

def main():
    octal_string = input("Enter a string of octal digits: ")
    decimal_value = octal_to_decimal(octal_string)
    print("The integer value is", decimal_value)

if __name__ == "__main__":
    main()
