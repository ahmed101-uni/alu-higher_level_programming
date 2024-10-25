#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0

    sum = 0
    weights = 0
    for i, j in my_list:
        sum += i * j
        weights += j

    return sum / weights
