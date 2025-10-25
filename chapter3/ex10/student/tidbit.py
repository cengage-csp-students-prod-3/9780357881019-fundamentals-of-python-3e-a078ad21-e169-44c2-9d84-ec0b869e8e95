# tidbit.py

price = float(input("Enter the purchase price: "))

# constants
down_payment = price * 0.10
balance = price - down_payment
monthly_payment = price * 0.05
monthly_rate = 0.12 / 12  # monthly interest rate

# header (must match exactly)
print("Month  Starting Balance  Interest to Pay  Principal to Pay  Payment  Ending Balance")

month = 1

while balance > 0:
    starting_balance = balance

    # interest this month
    interest = starting_balance * monthly_rate

    # tentative principal
    principal = monthly_payment - interest

    # if payment would exceed remaining balance, adjust last payment
    if monthly_payment >= balance:
        payment = balance
        # recalc principal so that interest + principal = payment
        interest = balance * monthly_rate
        principal = payment - interest
        # small rounding adjustment to avoid negative principal
        if principal < 0:
            principal = payment
            interest = 0.0
        ending_balance = 0.0
    else:
        payment = monthly_payment
        ending_balance = starting_balance - payment

    # round values for printing only
    print(f"{month:2d}         {starting_balance:7.2f}          {interest:5.2f}            {principal:6.2f}        {payment:6.2f}         {ending_balance:7.2f}")

    # prepare for next month
    balance = ending_balance
    month += 1
