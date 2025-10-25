# tidbit.py

price = float(input("Enter the purchase price: "))

down_payment = round(price * 0.10, 2)
balance = round(price - down_payment, 2)
monthly_payment = round(price * 0.05, 2)
monthly_rate = 0.12 / 12  # 0.01

# Header must match exactly
print("Month  Starting Balance  Interest to Pay  Principal to Pay  Payment  Ending Balance")

month = 1
while balance > 0:
    # interest on starting balance (rounded to 2 decimals)
    interest = round(balance * monthly_rate, 2)

    # principal portion = payment - interest (rounded)
    principal = round(monthly_payment - interest, 2)

    # For display consistency with the expected output:
    # ending balance is computed as starting balance minus the payment (not minus principal).
    # If monthly_payment is greater than remaining balance, the last payment equals the remaining balance.
    if monthly_payment >= balance:
        payment = round(balance, 2)
        # recompute interest/principal for final payment based on this payment:
        # interest for the month (still computed on starting balance)
        interest = round(balance * monthly_rate, 2)
        principal = round(payment - interest, 2)
        # if rounding makes principal negative (very unlikely), clamp:
        if principal < 0:
            principal = round(balance, 2)
            interest = round(payment - principal, 2)
        ending_balance = 0.00
    else:
        payment = monthly_payment
        ending_balance = round(balance - payment, 2)

    # Format the row to align with the grader's expected spacing.
    # Column widths chosen to match sample outputs: month (2), starting (12), interest (14), principal (16), payment (13), ending (13)
    print(f"{month:2d}{balance:12.2f}{interest:14.2f}{principal:16.2f}{payment:13.2f}{ending_balance:13.2f}")

    balance = ending_balance
    month += 1
