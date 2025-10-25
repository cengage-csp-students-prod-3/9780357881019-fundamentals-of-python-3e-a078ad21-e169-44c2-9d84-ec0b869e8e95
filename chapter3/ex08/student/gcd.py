
small = int(input("Enter the smaller number: "))
large = int(input("Enter the larger number: "))

while small != 0:
    remainder = large % small
    large, small = small, remainder

print("\nThe greatest common divisor is", large)
