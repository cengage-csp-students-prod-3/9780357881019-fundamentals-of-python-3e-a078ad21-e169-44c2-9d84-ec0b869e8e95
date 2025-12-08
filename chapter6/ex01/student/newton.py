# newton.py
#
# Newton’s Method for approximating square roots

def newton(x):
    """Returns the square root of x using Newton's method."""
    tolerance = 0.000001
    estimate = x / 2  # initial guess

    while True:
        new_estimate = (estimate + x / estimate) / 2
        if abs(new_estimate - estimate) < tolerance:
            return new_estimate
        estimate = new_estimate


def main():
    """Allows the user to compute square roots until the user quits."""
    while True:
        user_input = input("Enter a positive number or enter/return to quit: ")

        # Quit condition
        if user_input.strip() == "":
            break

        x = float(user_input)

        # Our estimate
        approx = newton(x)

        print(f"The program's estimate is {approx}")
        print(f"Python's estimate is      {x ** 0.5}")


if __name__ == "__main__":
    main()
