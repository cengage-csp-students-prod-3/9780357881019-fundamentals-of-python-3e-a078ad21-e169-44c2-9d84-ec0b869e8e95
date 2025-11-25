def isSorted(lst):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True

def main():
    # Test cases
    test_lists = [
        [],
        [1],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [1, 2, 2, 3],
        [1, 3, 2, 4]
    ]
    
    for lst in test_lists:
        print(f"List: {lst} -> Sorted? {isSorted(lst)}")

if __name__ == "__main__":
    main()
