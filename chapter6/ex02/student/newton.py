TOLERANCE = 1e-10

def limitReached(x, estimate):
    return abs(estimate * estimate - x) <= TOLERANCE

def improveEstimate(x, estimate):
    return (estimate + x / estimate) / 2

def newton(x):
    estimate = x / 2.0
    while not limitReached(x, estimate):
        estimate = improveEstimate(x, estimate)
    return estimate

def main():
    import math
    while True:
        user_input = input("Enter a positive number or enter/return to quit: ")
        if user_input == "":
            break
        try:
            number = float(user_input)
            if number <= 0:
                print("Please enter a positive number.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        estimate = newton(number)
        print("The program's estimate is", estimate)
        print("Python's estimate is     ", math.sqrt(number))

if __name__ == "__main__":
    main()
