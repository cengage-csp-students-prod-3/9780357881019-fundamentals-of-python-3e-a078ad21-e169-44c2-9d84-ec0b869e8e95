# bouncy.py

height = float(input("Enter the height from which the ball is dropped: "))
bounciness = float(input("Enter the bounciness index of the ball: "))
bounces = int(input("Enter the number of times the ball is allowed to continue bouncing: "))

total_distance = height

for i in range(bounces):
    height *= bounciness
    total_distance += 2 * height

print("Total distance traveled is:", total_distance, "units.")
