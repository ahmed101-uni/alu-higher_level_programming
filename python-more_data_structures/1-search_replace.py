#!/usr/bin/python3
def search_replace(my_list, search, replace):
    reps = [i for i, x in enumerate(my_list) if x == search]
    new_list = []
    for i, x in enumerate(my_list):
        if x == search:
            new_list.append(replace)
        else:
            new_list.append(x)

    return new_list
