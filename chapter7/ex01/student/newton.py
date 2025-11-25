def newton(x, estimate=None, tolerance=1e-10):
    if x < 0:
        raise ValueError("Cannot compute square root of a negative number.")
    if estimate is None:
        estimate = x / 2  # initial guess
    # check if estimate is close enough
    if abs(estimate * estimate - x) < tolerance:
        return estimate
    # recursive step: improve estimate
    return newton(x, (estimate + x / estimate) / 2, tolerance)

# Example usage
number = float(input("Enter a positive number or enter/return to quit: "))
if number > 0:
    approx = newton(number)
    print("The program's estimate is", approx)
    print("Python's estimate is     ", number ** 0.5)
