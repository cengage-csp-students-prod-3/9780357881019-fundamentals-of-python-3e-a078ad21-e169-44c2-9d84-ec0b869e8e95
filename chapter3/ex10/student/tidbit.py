# tidbit.py

price = float(input("Enter the purchase price: "))

# constants
down_payment = round(price * 0.10, 2)
balance = round(price - down_payment, 2)
monthly_payment = round(price * 0.05, 2)
monthly_rate = 0.12 / 12  # monthly interest rate

# header must match exactly
print("Month  Starting Balance  Interest to Pay  Principal to Pay  Payment  Ending Balance")

month = 1
while balance > 0:
    starting_balance = balance

    # interest on starting balance (rounded to cents)
    interest = round(starting_balance * monthly_rate, 2)

    # decide payment for this month (if remaining balance is smaller, pay remaining)
    if monthly_payment >= starting_balance:
        payment = round(starting_balance, 2)
    else:
        payment = monthly_payment

    # principal shown as payment minus interest (may be negative in odd rounding cases)
    principal = round(payment - interest, 2)

    # guard: if rounding makes principal negative, clamp principal to payment and set interest to 0.00
    if principal < 0:
        principal = round(payment, 2)
        interest = 0.00

    # IMPORTANT: according to the provided sample outputs, Ending Balance = Starting Balance - Payment
    ending_balance = round(starting_balance - payment, 2)

    # tiny correction to avoid printing -0.00
    if abs(ending_balance) < 0.005:
        ending_balance = 0.00

    # print row using widths that match the sample formatting (two decimals)
    print(f"{month:2d} {starting_balance:15.2f} {interest:17.2f} {principal:17.2f} {payment:9.2f} {ending_balance:15.2f}")

    # prepare for next month
    balance = ending_balance
    month += 1
