# sevens.py
import random

def main():
    # get initial money from user
    try:
        pot = int(input("How many dollars do you have? "))
        if pot <= 0:
            print("Please enter a positive amount.")
            return
    except ValueError:
        print("Please enter an integer amount.")
        return

    starting_pot = pot
    max_pot = pot
    roll_count = 0
    rolls_at_max = 0

    while pot > 0:
        roll_count += 1

        # roll two dice
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        total = die1 + die2

        if total == 7:
            pot += 4  # win $4
        else:
            pot -= 1  # lose $1

        # track max pot
        if pot > max_pot:
            max_pot = pot
            rolls_at_max = roll_count

    # output results
    print(f"\nYou are broke after {roll_count} rolls.")
    print(f"You should have quit after {rolls_at_max} rolls when you had ${max_pot}.")

if __name__ == "__main__":
    main()
