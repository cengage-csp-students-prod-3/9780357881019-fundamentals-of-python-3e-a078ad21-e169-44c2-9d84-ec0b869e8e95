"""
File: student_comparison.py
Adds comparison methods to the Student class and tests them.
"""

class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    # Equality operator: compares names
    def __eq__(self, other):
        if isinstance(other, Student):
            return self.name == other.name
        return NotImplemented

    # Less than operator: compares names
    def __lt__(self, other):
        if isinstance(other, Student):
            return self.name < other.name
        return NotImplemented

    # Greater than or equal operator: compares names
    def __ge__(self, other):
        if isinstance(other, Student):
            return self.name >= other.name
        return NotImplemented


def main():
    # Create sample students
    s1 = Student("Alice", 90)
    s2 = Student("Bob", 85)
    s3 = Student("Alice", 95)

    # Test equality (__eq__)
    print(s1 == s2, s1 == s3)  # False: True

    # Test less than (__lt__)
    print(s1 < s2, s2 < s1)    # True: False

    # Test greater than or equal (__ge__)
    print(s1 >= s2, s2 >= s1)  # False: True

    # Additional tests
    students = [s1, s2, s3]
    for i in students:
        for j in students:
            print(i >= j, i == j)

if __name__ == "__main__":
    main()
