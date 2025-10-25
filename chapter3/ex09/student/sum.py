
total = 0.0
count = 0

while True:
    data = input("Enter a number or press Enter to quit: ")
    if data == "":
        break
    number = float(data)
    total += number
    count += 1

if count > 0:
    average = total / count
    print("\nThe sum is", total)
    print("The average is", average)
else:
    print("\nNo numbers were entered.")
