TOLERANCE = 1e-7

def limitReached(x, estimate):
    if abs(estimate**2 - x) <= TOLERANCE:
        return 1  # True yerine 1 döndür
    else:
        return 0  # False yerine 0 döndür

def improveEstimate(x, estimate):
    return (estimate + x / estimate) / 2

def newton(x):
    if x <= 0:
        return 0
    estimate = x / 2  # Başlangıç tahmini
    while not limitReached(x, estimate):
        estimate = improveEstimate(x, estimate)
    return estimate

def main():
    while True:
        inp = input("Enter a positive number or enter/return to quit: ")
        if inp == "":
            break
        try:
            num = float(inp)
            estimate = newton(num)
            print("The program's estimate is", estimate)
            print("Python's estimate is     ", num**0.5)
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()
