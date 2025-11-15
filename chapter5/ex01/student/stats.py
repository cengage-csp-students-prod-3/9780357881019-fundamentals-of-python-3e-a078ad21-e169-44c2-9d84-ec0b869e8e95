# Write your program here
# stats.py

def mean(numbers):
    """Return the mean (average) of the list. Return 0 if empty."""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


def median(numbers):
    """Return the median of the list. Return 0 if empty."""
    if not numbers:
        return 0
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    mid = n // 2
    if n % 2 == 0:
        
        return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
    else:
       
        return sorted_nums[mid]


def mode(numbers):
    """Return the mode of the list. Return 0 if empty. If multiple, return the first."""
    if not numbers:
        return 0
    counts = {}
    for num in numbers:
        counts[num] = counts.get(num, 0) + 1
    
    max_count = max(counts.values())
    for num in numbers:  
        if counts[num] == max_count:
            return num


def main():
    nums = [8, 2, 5, 3, 9, 6, 2, 7]
    print("List:", nums)
    print("Mode:", mode(nums))
    print("Median:", median(nums))
    print("Mean:", mean(nums))


if __name__ == "__main__":
    main()
