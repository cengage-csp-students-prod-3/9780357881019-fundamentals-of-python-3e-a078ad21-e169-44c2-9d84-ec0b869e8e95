def limitReached(estimate, number):
    return abs(number - estimate ** 2) < 1e-15

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
        initial_guess = number / 2
        estimate = newton(initial_guess, number)

        # Birebir string match için float’ı direkt print ediyoruz
        print("The program's estimate is", estimate)
        print("Python's estimate is      ", number ** 0.5)

if __name__ == "__main__":
    main()
