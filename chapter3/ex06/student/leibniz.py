
iterations = int(input("Enter the number of iterations: "))

pi_approx = 0.0
sign = 1

for i in range(iterations):
    pi_approx += sign * (1 / (2 * i + 1))
    sign *= -1

pi_approx *= 4

print("The approximation of pi is", pi_approx)
