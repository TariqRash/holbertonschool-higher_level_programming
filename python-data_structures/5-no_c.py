#!/usr/bin/python3
def no_c(my_string):
    """Remove all characters 'c' and 'C' from a string."""
    new_string = ""
    for ch in my_string:
        if ch != 'c' and ch != 'C':
            new_string += ch
    return new_string
