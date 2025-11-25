def newton(x, estimate=None):
    """Recursively estimates the square root of x using Newton's method."""
    if x == 0:
        return 0
    if estimate is None:
        estimate = x / 2  # initial guess
    if abs(estimate**2 - x) < 1e-8:  # tolerance for stopping
        return estimate
    new_estimate = (estimate + x / estimate) / 2
    return newton(x, new_estimate)

def main():
    import math
    while True:
        user_input = input("Enter a positive number or enter/return to quit: ")
        if user_input == "":
            break
        try:
            x = float(user_input)
            if x < 0:
                print("Please enter a positive number.")
                continue
            estimate = newton(x)
            print("The program's estimate is", estimate)
            print("Python's estimate is     ", math.sqrt(x))
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
