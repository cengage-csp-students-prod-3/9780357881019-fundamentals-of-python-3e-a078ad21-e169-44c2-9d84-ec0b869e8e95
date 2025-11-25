# testinputfunctions.py

def inputFloat(prompt="Please enter an integer or a float: "):
    """Prompts the user until they enter a valid float."""

    while True:
        user_input = input(prompt)

        # Count decimal points
        if user_input.count('.') > 1:
            print("Error: the input cannot have more than one '.'")
            continue

        # Remove ONE decimal point for digit check
        stripped = user_input.replace('.', '', 1)

        # Check if all remaining characters are digits
        if not stripped.isdigit():
            print("Error: the input must consist only of digits")
            continue

        # Convert to float and return
        return float(user_input)


# ----------------------
# Testing the function
# ----------------------
def main():
    value = inputFloat()
    print(value)


if __name__ == "__main__":
    main()
