
import math

low = int(input("Enter the smaller number: "))
high = int(input("Enter the larger number: "))

max_guesses = math.ceil(math.log(high - low + 1, 2))
count = 0

while low <= high and count < max_guesses:
    print(low, high)
    guess = (low + high) // 2
    print("Your number is", guess)
    result = input("Enter =, <, or >: ")
    count += 1

    if result == "=":
        print(f"Hooray, I've got it in {count} tries!")
        break
    elif result == "<":
        high = guess - 1
    elif result == ">":
        low = guess + 1
    else:
        print("Invalid input. Please enter =, <, or >.")

else:
    print("I'm out of guesses, and you cheated!")
