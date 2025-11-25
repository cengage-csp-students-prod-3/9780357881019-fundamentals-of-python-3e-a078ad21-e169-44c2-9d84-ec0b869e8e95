def newton(x):
    estimate = x / 2.0
    tolerance = 1e-10
    while abs(estimate * estimate - x) > tolerance:
        estimate = (estimate + x / estimate) / 2
    return estimate

def main():
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
        import math
        print("The program's estimate is", estimate)
        print("Python's estimate is     ", math.sqrt(number))

if __name__ == "__main__":
    main()
