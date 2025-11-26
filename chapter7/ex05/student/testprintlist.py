def printAll(seq):
    # Trace the argument at the start of each call
    print(f"Calling printAll with: {seq}")
    
    if seq:  # If the sequence is not empty
        print(seq[0])  # Print the first element
        printAll(seq[1:])  # Recursive call with the rest of the sequence

# Test the function
if __name__ == "__main__":
    # Test with a list
    test_list = [1, 2, 3, 4]
    print("Testing with a list:")
    printAll(test_list)

    # Test with a string
    test_string = "hello"
    print("\nTesting with a string:")
    printAll(test_string)

    # Test with a tuple
    test_tuple = ('a', 'b', 'c')
    print("\nTesting with a tuple:")
    printAll(test_tuple)
