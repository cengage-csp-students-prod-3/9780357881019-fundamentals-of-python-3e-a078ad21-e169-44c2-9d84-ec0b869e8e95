"""
File: newton.py
Restructured version of Newton's method using recursion.
"""

# --------------------------------------------
# Checks whether the approximation is close enough
# --------------------------------------------
def limitReached(estimate, number):
    return abs(number - estimate ** 2) < 0.000001   # tolerance

# --------------------------------------------
# Computes an improved approximation
# --------------------------------------------
def improveEstimate(estimate, number):
    return (estimate + number / estimate) / 2

# --------------------------------------------
# Recursive Newton function
# --------------------------------------------
def newton(estimate, number):
    if limitReached(estimate, number):
        return estimate
    else:
        return newton(improveEstimate(estimate, number), number)

# --------------------------------------------
# Main input loop
# --------------------------------------------
def main():
    while True:
        user_input = input("Enter a positive number or enter/return to quit: ")

        if user_input == "":
            break

        number = float(user_input)
        initial_guess = number / 2

        estimate = newton(initial_guess, number)

        print("The program's estimate is", estimate)
        print("Python's estimate is     ", number ** 0.5)

if __name__ == "__main__":
    main()
