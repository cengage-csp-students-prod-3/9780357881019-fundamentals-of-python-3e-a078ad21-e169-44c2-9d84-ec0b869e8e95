# hof.py
# Higher-order function implementations

def myMap(func, lst):
    """Apply func to each element of lst and return a new list."""
    result = []
    for item in lst:
        result.append(func(item))
    return result

def myFilter(func, lst):
    """Return a list of elements in lst for which func(item) is True."""
    result = []
    for item in lst:
        if func(item):
            result.append(item)
    return result

def myReduce(func, lst):
    """Apply func cumulatively to the items of lst, from left to right, to reduce to a single value."""
    if not lst:
        raise ValueError("myReduce() of empty sequence with no initial value")
    result = lst[0]
    for item in lst[1:]:
        result = func(result, item)
    return result
