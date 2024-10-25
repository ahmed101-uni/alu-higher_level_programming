#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newdict = {}
    for i, x in a_dictionary.items():
        x *= 2
        newdict[i] = x

    return newdict
