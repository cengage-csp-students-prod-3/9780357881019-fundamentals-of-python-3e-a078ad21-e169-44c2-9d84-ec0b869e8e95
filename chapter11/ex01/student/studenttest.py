# studenttest.py
# Tests the Student class from the Analyzing Student Test Scores case study.

from student import Student

def main():
    # Create a student object with no initial random scores
    student = Student("Test Student", 0)

    # Example data given in assignment instructions
    scores = [82, 76, 77, 93, 97, 97, 90, 98, 83, 88]

    # Add scores to model
    for score in scores:
        student.addScore(score)

    # Print positions and scores
    print("Position Score")
    position = 1
    for score in student._scores:   # model already stores list internally
        print(f"{position:7d}{score:8d}")
        position += 1

    # Print statistics
    print("\nMean:", student.getMean())
    print("Median:", student.getMedian())
    print("Mode:", student.getMode())
    print("Standard deviation:", student.getStd())

if __name__ == "__main__":
    main()

