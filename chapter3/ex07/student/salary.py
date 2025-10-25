
starting_salary = float(input("Enter the starting salary: $"))
percent_increase = float(input("Enter the annual % increase: "))
years = int(input("Enter the number of years: "))

print("\nYear   Salary")
print("-------------")

salary = starting_salary

for year in range(1, years + 1):
    print(f"{year:2d}    {salary:.2f}")
    salary *= (1 + percent_increase / 100)
