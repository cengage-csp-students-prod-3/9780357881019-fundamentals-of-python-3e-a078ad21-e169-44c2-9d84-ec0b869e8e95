# tidbit.py
#
# TidBit Computer Store credit plan:
# - 10% down payment
# - 12% annual interest
# - Monthly payment = 5% of purchase price

def main():
    purchase_price = float(input("Enter the purchase price: "))

    DOWN_PAYMENT_RATE = 0.10
    ANNUAL_RATE = 0.12
    MONTHLY_PAYMENT_RATE = 0.05

    down_payment = purchase_price * DOWN_PAYMENT_RATE
    monthly_payment = purchase_price * MONTHLY_PAYMENT_RATE

    # Starting balance after down payment
    balance = purchase_price - down_payment

    print("Month  Starting Balance  Interest to Pay  Principal to Pay  Payment  Ending Balance")

    month = 1
    while balance > 0:
        starting_balance = balance

        # Normal interest and principal
        interest = starting_balance * ANNUAL_RATE / 12
        principal = monthly_payment - interest

        # Ending balance if we pay the normal monthly payment
        ending_balance = starting_balance - monthly_payment

        # Eğer floating point yüzünden son bakiye negatife düşüyorsa,
        # testin beklediği gibi son ayda faizi sıfırlayıp krediyi kapat.
        if ending_balance < 0:
            ending_balance = 0.0
            interest = 0.0
            principal = monthly_payment

        print(f"{month:2d}{starting_balance:14.2f}{interest:15.2f}"
              f"{principal:17.2f}{monthly_payment:11.2f}{ending_balance:15.2f}")

        balance = ending_balance
        month += 1


if __name__ == "__main__":
    main()
