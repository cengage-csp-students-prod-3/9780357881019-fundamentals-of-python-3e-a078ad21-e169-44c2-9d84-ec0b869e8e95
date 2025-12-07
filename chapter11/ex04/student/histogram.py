"""
File: histogram.py
Displays a histogram of example scores.
"""

import matplotlib.pyplot as plt

def main():
    # Example data (can be adjusted to match Figure 11-7)
    scores = [82, 76, 77, 93, 97, 97, 90, 98, 83, 88,
              65, 70, 72, 85, 91, 92, 78, 80, 84, 87]

    # Number of bins (adjust to match figure)
    num_bins = 10

    # Create histogram
    plt.figure(figsize=(7,4))
    plt.hist(scores, bins=num_bins, color='skyblue', edgecolor='black')
    plt.title("Histogram of Student Scores")
    plt.xlabel("Score")
    plt.ylabel("Number of Students")
    plt.grid(axis='y', alpha=0.75)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
