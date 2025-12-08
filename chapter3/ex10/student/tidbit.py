# tidbit.py
#
# TidBit Computer Store credit plan:
# - 10% down payment
# - 12% annual interest
# - Monthly payment = 5% of purchase price

def main():
    purchase_price = float(input("Enter the purchase price: "))

    # Sabitler
    DOWN_PAYMENT_RATE = 0.10
    ANNUAL_RATE = 0.12
    MONTHLY_PAYMENT_RATE = 0.05

    down_payment = purchase_price * DOWN_PAYMENT_RATE
    monthly_payment = purchase_price * MONTHLY_PAYMENT_RATE

    # Başlangıç bakiyesi (peşinat ödenmiş)
    balance = purchase_price - down_payment

    print("Month  Starting Balance  Interest to Pay  Principal to Pay  Payment  Ending Balance")

    month = 1
    # Borç bitene kadar tabloyu yaz
    while balance > 0:
        starting_balance = balance

        # Aylık faiz
        interest = starting_balance * ANNUAL_RATE / 12

        # O ayki anapara (ödeme – faiz)
        principal = monthly_payment - interest

        # Örnek tabloda olduğu gibi: bitiş bakiyesi = başlangıç – aylık ödeme
        ending_balance = starting_balance - monthly_payment
        if ending_balance < 0:
            ending_balance = 0.0

        # Satırı yazdır
        print(f"{month:2d}{starting_balance:14.2f}{interest:15.2f}"
              f"{principal:17.2f}{monthly_payment:11.2f}{ending_balance:15.2f}")

        # Sonraki ay için güncelle
        balance = ending_balance
        month += 1


if __name__ == "__main__":
    main()
