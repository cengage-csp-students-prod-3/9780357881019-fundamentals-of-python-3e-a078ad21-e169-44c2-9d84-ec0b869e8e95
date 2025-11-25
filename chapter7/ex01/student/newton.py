def newton(x, estimate=None, tolerance=1e-10):
    """
    Recursively approximates the square root of x using Newton's method.
    
    Parameters:
    x         : The number to find the square root of (positive float or int)
    estimate  : Current estimate of the square root (default: x/2)
    tolerance : Acceptable error margin (default: 1e-10)
    
    Returns:
    A float approximating the square root of x.
    """
    if estimate is None:
        estimate = x / 2  # initial guess
    if abs(estimate * estimate - x) < tolerance:
        return estimate
    return newton(x, (estimate + x / estimate) / 2, tolerance)

# Example usage (for manual testing)
if __name__ == "__main__":
    x = float(input("Enter a positive number or enter/return to quit: "))
    print("The program's estimate is", newton(x))
