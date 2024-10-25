#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    reps = [i for i, x in a_dictionary.items() if x == value]

    for i in reps:
        a_dictionary.pop(i)

    return a_dictionary
