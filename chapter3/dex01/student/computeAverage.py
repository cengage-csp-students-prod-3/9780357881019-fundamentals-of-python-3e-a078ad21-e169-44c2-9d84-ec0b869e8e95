count = 1
total = 0
while count <= 10:  # use <= to include 10th score
    score = int(input("Enter test score number " + str(count) + ": "))
    total = total + score
    count = count + 1

average = total / 10  # divide by 10 because we are collecting 10 scores
print("The average test score is", average)
