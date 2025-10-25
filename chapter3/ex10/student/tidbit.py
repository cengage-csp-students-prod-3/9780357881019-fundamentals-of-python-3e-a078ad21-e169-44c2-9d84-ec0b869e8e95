# tidbit.py

# Get user input
price = float(input("Enter the purchase price: "))

# Calculate down payment and initial balance
down_payment = price * 0.10
balance = round(price - down_payment, 2)

# Constants
annual_interest_rate = 0.12
monthly_payment = round(price * 0.05, 2)

# Print table header
print("Month  Starting Balance  Interest to Pay  Principal to Pay  Payment  Ending Balance")

month = 1

# Loop until balance is paid off
while balance > 0:
    interest = round(balance * (annual_interest_rate / 12), 2)
    principal = round(monthly_payment - interest, 2)

    # Adjust for the last payment if needed
    if principal > balance:
        principal = balance
        monthly_payment = round(interest + principal, 2)

    ending_balance = round(balance - principal, 2)

    print(f"{month:2d}       {balance:8.2f}           {interest:5.2f}             {principal:5.2f}        {monthly_payment:6.2f}          {ending_balance:8.2f}")

    balance = ending_balance
    month += 1
