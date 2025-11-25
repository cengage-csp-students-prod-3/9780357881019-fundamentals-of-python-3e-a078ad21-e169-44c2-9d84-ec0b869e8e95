# newton.py

TOLERANCE = 1e-7

def limitReached(x, estimate):
    return abs(estimate**2 - x) <= TOLERANCE

def improveEstimate(x, estimate):
    return (estimate + x / estimate) / 2

def newton(x):
    estimate = x / 2 if x != 0 else 0
    while not limitReached(x, estimate):
        estimate = improveEstimate(x, estimate)
    return estimate

def main():
    while True:
        user_input = input("Enter a positive number or enter/return to quit: ")
        if user_input == "":
            break
        try:
            num = float(user_input)
            if num < 0:
                print("Please enter a positive number.")
                continue
            estimate = newton(num)
            print(f"The program's estimate is {estimate}")
            import math
            print(f"Python's estimate is      {math.sqrt(num)}")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
