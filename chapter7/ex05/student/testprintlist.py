def printAll(seq):
    """Prints the sequence recursively, with each line shorter than the previous one."""
    if seq:
        print(seq)       # Print the current sequence
        printAll(seq[1:])  # Recursive call with the rest of the sequence

# Test the function
if __name__ == "__main__":
    test_list = [1, 2, 3, 4]
    printAll(test_list)
