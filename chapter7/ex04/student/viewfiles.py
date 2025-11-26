def printAll(seq):
    print(f"Calling printAll with: {seq}")  # Trace the argument
    if seq:
        print(seq[0])  # Print the first element
        printAll(seq[1:])  # Recursive call with the rest of the sequence

# Test the function
if __name__ == "__main__":
    test_seq = ['a', 'b', 'c', 'd']
    print("Testing with a list:")
    printAll(test_seq)
    
    print("\nTesting with a string:")
    printAll("hello")
    
    print("\nTesting with a tuple:")
    printAll((1, 2, 3))
