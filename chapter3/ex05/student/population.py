
initial = int(input("Enter the initial number of organisms: "))
rate = float(input("Enter the rate of growth [a real number > 1]: "))
hours_to_rate = float(input("Enter the number of hours to achieve the rate of growth: "))
total_hours = float(input("Enter the total hours of growth: "))

periods = total_hours / hours_to_rate
population = initial * (rate ** periods)

print("The total population is", int(population))
