#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """Find all multiples of 2 in a list.

    Return a list of booleans with same size as original.
    """
    result = []
    for number in my_list:
        result.append(number % 2 == 0)
    return result
