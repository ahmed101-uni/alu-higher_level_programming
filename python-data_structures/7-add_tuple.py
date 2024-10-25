#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    [a, b] = [list(tuple_a), list(tuple_b)]
    if len(a) < 2:
        for i in range(2 - len(a)):
            a.append(0)
    if len(b) < 2:
        for i in range(2 - len(b)):
            b.append(0)

    result = (a[0] + b[0], a[1] + b[1])
    return result
