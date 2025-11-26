"""
File: newton.py
Restructured version of Newton's method using recursion.
"""

def limitReached(estimate, number):
    return abs(number - estimate ** 2) < 1e-14   # çok daha küçük tolerans

def improveEstimate(estimate, number):
    return (estimate + number / estimate) / 2

def newton(estimate, number):
    if limitReached(estimate, number):
        return estimate
    return newton(improveEstimate(estimate, number), number)

def main():
    while True:
        user_input = input("Enter a positive number or enter/return to quit: ")

        if user_input == "":
            break

        number = float(user_input)
        estimate = newton(number / 2, number)

        print(f"The program's estimate is {estimate}")
        print(f"Python's estimate is      {number ** 0.5}")

if __name__ == "__main__":
    main()
