# tidbit.py

price = float(input("Enter the purchase price: "))

# constants from the problem
down_payment = round(price * 0.10, 2)
balance = round(price - down_payment, 2)
monthly_payment = round(price * 0.05, 2)
monthly_rate = 0.12 / 12  # monthly interest rate

# header (must match exactly)
print("Month  Starting Balance  Interest to Pay  Principal to Pay  Payment  Ending Balance")

month = 1
# iterate until the balance reaches zero
while balance > 0:
    # compute interest on the current starting balance (rounded to 2 decimals)
    interest = round(balance * monthly_rate, 2)

    # compute principal portion as payment minus interest
    principal = round(monthly_payment - interest, 2)

    # If the standard monthly payment is greater than the remaining balance,
    # adjust the final payment and principal so the loan finishes at 0.00.
    if monthly_payment >= balance:
        # final payment equals the remaining balance
        payment = round(balance, 2)
        # For display, compute interest on the current balance (rounded).
        # Then principal is payment - interest (but ensure non-negative).
        # If this would produce a negative principal because interest > payment,
        # set interest to the rounded monthly interest and principal to the remainder (or the balance).
        interest = round(balance * monthly_rate, 2)
        principal = round(payment - interest, 2)
        # If rounding makes principal negative (rare), clamp it to balance and set interest = payment - principal
        if principal < 0:
            principal = round(balance, 2)
            interest = round(payment - principal, 2)
        ending_balance = 0.00
    else:
        payment = monthly_payment
        ending_balance = round(balance - payment, 2)

    # Print formatted row to match the example layout
    print(f"{month:2d}         {balance:7.2f}          {interest:5.2f}            {principal:6.2f}        {payment:6.2f}         {ending_balance:7.2f}")

    # prepare for next month
    balance = ending_balance
    month += 1
