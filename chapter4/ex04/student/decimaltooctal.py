# decimaltooctal.py
# Converts a decimal integer to octal

def decimal_to_octal(decimal_number):
    if decimal_number == 0:
        return "0"
    
    octal_digits = ""
    while decimal_number > 0:
        remainder = decimal_number % 8
        octal_digits = str(remainder) + octal_digits
        decimal_number = decimal_number // 8
    return octal_digits

def main():
    decimal_number = int(input("Enter a decimal integer: "))
    octal_number = decimal_to_octal(decimal_number)
    print("The octal representation is", octal_number)

if __name__ == "__main__":
    main()
