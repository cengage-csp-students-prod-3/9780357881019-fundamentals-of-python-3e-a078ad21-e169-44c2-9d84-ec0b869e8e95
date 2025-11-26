"""
File: newton.py
Recursive Newton method with exact output formatting.
"""

# --------------------------------------------
# Checks whether the approximation is close enough
# --------------------------------------------
def limitReached(estimate, number):
    # Çok küçük tolerans ile örnekle aynı sonucu yakalıyoruz
    return abs(number - estimate ** 2) < 1e-15

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
        initial_guess = number / 2   # Örnek programda kullanılan başlangıç tahmini

        estimate = newton(initial_guess, number)

        # Çıktıyı birebir örnekle aynı yapmak için 16 basamak kullanıyoruz
        print(f"The program's estimate is {estimate:.16f}")
        print(f"Python's estimate is      {number**0.5:.16f}")

if __name__ == "__main__":
    main()
