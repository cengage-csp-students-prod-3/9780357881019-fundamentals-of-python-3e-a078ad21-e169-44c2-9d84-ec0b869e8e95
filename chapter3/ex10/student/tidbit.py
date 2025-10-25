price = float(input("Enter the purchase price: "))

down_payment = round(price * 0.10, 2)
balance = round(price - down_payment, 2)
monthly_payment = round(price * 0.05, 2)
monthly_rate = 0.12 / 12  # monthly interest rate


print("Month  Starting Balance  Interest to Pay  Principal to Pay  Payment  Ending Balance")

month = 1

while balance > 0:
    starting_balance = round(balance, 2)

    if balance <= monthly_payment:
        payment = round(balance, 2)
        interest = 0.00           
        principal = payment      
        ending_balance = 0.00
    else:
        
        interest = round(starting_balance * monthly_rate, 2)
        principal = round(monthly_payment - interest, 2)
        payment = monthly_payment
        ending_balance = round(starting_balance - payment, 2)

    
    print(f"{month:2d}         {starting_balance:7.2f}          {interest:5.2f}            {principal:6.2f}        {payment:6.2f}         {ending_balance:7.2f}")

    balance = ending_balance
    month += 1
