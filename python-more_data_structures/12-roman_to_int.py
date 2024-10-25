#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str or not roman_string:
        return 0

    roms = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    num = 0
    for i, x in enumerate(roman_string):
        num += roms[x]
        if i != 0 and roms[roman_string[i-1]] < roms[x]:
            num -= 2 * roms[roman_string[i-1]]

    return num


# Beneath are the remains of the initial way I tried to solve this.

# if x == "I":
#     if i != len(roman_string)- 1 and roman_string[i+1] not in ["V", "X"]:
#         num += 1

# if x == "V":
#     if roman_string[i-1] == "I":
#         num += 4
#     else:
#         num += 5

# if x == "X":
#     if i != len(roman_string)- 1 and roman_string[i+1] not in ["L", "C"]:
#         if roman_string[i-1] == "I":
#             num += 9
#         else:
#             num += 10

# if x == "L":
#     if roman_string[i-1] == "X":
#         num += 40
#     else:
#         num += 50

# if x == "C":
#     if i != len(roman_string)- 1 and roman_string[i+1] not in ["D", "M"]:
#         if roman_string[i-1] == "X":
#             num += 90
#         else:
#             num += 100

# if x == "D":
#     if roman_string[i-1] == "C":
#         num += 400
#     else:
#         num += 500

# if x == "M":
#     if roman_string[i-1] == "C":
#         num += 900
#     else:
#         num += 1000
