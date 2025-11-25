# convert.py

# Lookup table for digits 0-9 and letters A-F
digit_values = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
    '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}

def repToDecimal(s, base):
    """Convert a number in a given base (as a string) to decimal."""
    s = s.upper()  # Ensure letters are uppercase
    decimal_value = 0
    power = len(s) - 1  # Start from the leftmost digit
    
    for digit in s:
        if digit not in digit_values or digit_values[digit] >= base:
            raise ValueError(f"Invalid digit '{digit}' for base {base}")
        decimal_value += digit_values[digit] * (base ** power)
        power -= 1
    
    return decimal_value

def main():
    # Test the function with different bases
    print(repToDecimal("10", 2))   # binary 10 → 2
    print(repToDecimal("10", 8))   # octal 10 → 8
    print(repToDecimal("10", 16))  # hex 10 → 16
    print(repToDecimal("1F", 16))  # hex 1F → 31
    print(repToDecimal("101", 2))  # binary 101 → 5
    print(repToDecimal("77", 8))   # octal 77 → 63

if __name__ == "__main__":
    main()

