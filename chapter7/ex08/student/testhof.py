# testhof.py
from hof import myMap, myFilter, myReduce
from functools import reduce  # Python's built-in reduce

# Test data
test_lists = [
    [0, 1, 2, 3, 4],
    [3],
    []
]

def square(x):
    return x ** 2

def is_odd(x):
    return x % 2 == 1

def add(x, y):
    return x + y

for lst in test_lists:
    print(f"Argument list:   {lst}")
    
    # Test map
    print("map with ** 2  :", list(map(square, lst)))
    print("myMap with ** 2:", myMap(square, lst))
    
    # Test filter
    print("filter with odd  :", list(filter(is_odd, lst)))
    print("myFilter with odd:", myFilter(is_odd, lst))
    
    # Test reduce (handle empty list safely)
    if lst:
        print("reduce with +   :", reduce(add, lst))
        print("myReduce with + :", myReduce(add, lst))
    print()
