#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    total = sum(s * w for s, w in my_list)
    weights = sum(w for s, w in my_list)
    return total / weights
