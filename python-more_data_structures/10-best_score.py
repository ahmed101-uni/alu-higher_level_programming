#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        sortdict = sorted(a_dictionary.items(),
                          key=lambda i: i[1], reverse=True)
        return sortdict[0][0]

    return None
