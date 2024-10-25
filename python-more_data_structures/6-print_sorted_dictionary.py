#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    newdict = sorted(a_dictionary.items(), key=lambda i: i[0])

    for i, x in newdict:
        print("{}: {}".format(i, x))
