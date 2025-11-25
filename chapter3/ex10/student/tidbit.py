"""
Program: tidbit.py
Author: Your Name
Displays a payment schedule for TidBit Computer Store credit plan.
"""

# Sabitler
DOWN_PAYMENT_RATE = 0.10      # %10 peşinat
ANNUAL_INTEREST_RATE = 0.12   # %12 yıllık faiz
MONTHLY_PAYMENT_RATE = 0.05   # %5 aylık ödeme (liste fiyatına göre)

# Kullanıcıdan satın alma fiyatını al
purchase_price = float(input("Enter the purchase price: "))

# Peşinat sonrası kalan bakiye
balance = purchase_price * (1 - DOWN_PAYMENT_RATE)

# Sabit aylık ödeme
monthly_payment = purchase_price * MONTHLY_PAYMENT_RATE

# Tablo başlıkları
print(f"{'Month':<6}{'Starting Balance':<18}{'Interest to Pay':<18}"
      f"{'Principal to Pay':<18}{'Payment':<10}{'Ending Balance':<15}")

month = 1
while balance > 0:
    interest = balance * ANNUAL_INTEREST_RATE / 12
    principal = monthly_payment - interest
    
    # Eğer principal, kalan bakiyeden büyükse, son ödeme olarak düzelt
    if principal > balance:
        principal = balance
        monthly_payment = interest + principal
    
    ending_balance = balance - principal
    
    print(f"{month:<6}{balance:>14.2f}{interest:>18.2f}{principal:>18.2f}"
          f"{monthly_payment:>10.2f}{ending_balance:>15.2f}")
    
    balance = ending_balance
    month += 1
