def newton(x):
    estimate = x / 2.0  # initial guess, matches the case study
    while True:
        new_estimate = (estimate + x / estimate) / 2
        if abs(new_estimate - estimate) < 1e-10:  # stop when estimate stabilizes
            break
        estimate = new_estimate
    return estimate

def main():
    while True:
        user_input = input("Enter a positive number or enter/return to quit: ")
        if user_input == "":
            break
        try:
            num = float(user_input)
            if num <= 0:
                print("Please enter a positive number.")
                continue
            estimate = newton(num)
            print("The program's estimate is", estimate)
            print("Python's estimate is      ", num**0.5)
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
