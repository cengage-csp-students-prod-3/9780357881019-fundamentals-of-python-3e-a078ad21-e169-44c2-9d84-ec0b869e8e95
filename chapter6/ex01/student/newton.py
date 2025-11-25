def newton(x):
    estimate = 1.0  # start with 1.0 to match the case study
    while True:
        new_estimate = (estimate + x / estimate) / 2
        if abs(new_estimate - estimate) < 1e-12:  # very small tolerance
            break
        estimate = new_estimate
    return new_estimate

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
