# tidbit.py
def main():
    price_input = input("Enter the purchase price: ")
    try:
        price = float(price_input)
        if price <= 0:
            raise ValueError
    except ValueError:
        print("Please enter a positive numeric purchase price.")
        return

    down_payment_rate = 0.10          # 10% down
    annual_rate = 0.12                # 12% annual interest
    monthly_payment_rate = 0.05       # 5% of listed purchase price (fixed each month)

    down_payment = price * down_payment_rate
    balance = price - down_payment
    monthly_payment = price * monthly_payment_rate

    # Print header
    print("Month  Starting Balance  Interest to Pay  Principal to Pay  Payment  Ending Balance")

    month = 1
    # Loop until balance is essentially zero
    while balance > 0.0005:
        starting_balance = balance
        interest = starting_balance * annual_rate / 12.0

        # If the regular payment would pay more than remaining balance+interest,
        # make a final adjusted payment so ending balance becomes exactly zero.
        if monthly_payment >= starting_balance + interest - 1e-12:
            principal = starting_balance
            payment = interest + principal
            ending_balance = 0.0
        else:
            payment = monthly_payment
            principal = payment - interest
            ending_balance = starting_balance - principal

        # Print row with two-decimal alignment matching the example
        print(f"{month:2d} {starting_balance:15.2f} {interest:17.2f} {principal:17.2f} {payment:9.2f} {ending_balance:15.2f}")

        # prepare next month
        balance = ending_balance
        month += 1


if __name__ == "__main__":
    main()
