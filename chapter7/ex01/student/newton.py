import math

def newton(x, estimate=None, tolerance=1e-12):
    if estimate is None:
        estimate = x / 2 if x != 0 else 0
    # Check if current estimate is good enough
    if abs(estimate**2 - x) < tolerance:
        return estimate
    # Recursive step
    new_estimate = (estimate + x / estimate) / 2
    return newton(x, new_estimate, tolerance)

def main():
    while True:
        user_input = input("Enter a positive number or enter/return to quit: ")
        if not user_input:
            print("Goodbye!")
            break
        try:
            x = float(user_input)
            if x < 0:
                print("Please enter a positive number.")
                continue
            estimate = newton(x)
            print(f"The program's estimate is {estimate:.12f}")
            print(f"Python's estimate is      {math.sqrt(x):.12f}")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
