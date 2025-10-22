
side1 = float(input("Enter the first side: "))
side2 = float(input("Enter the second side: "))
side3 = float(input("Enter the third side: "))


a, b, c = sorted([side1, side2, side3])


if abs(c**2 - (a**2 + b**2)) < 1e-6:
    print("The triangle is a right triangle.")
else:
    print("The triangle is not a right triangle.")
