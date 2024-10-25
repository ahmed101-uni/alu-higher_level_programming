#!/usr/bin/python3
import random
number = random.randint(-10, 10)

print(number, "is", "positive" if number > 0
      else "negative" if number < 0 else "zero")


# This is the normal way of doing it, but I just wanted to use ternery operator
# if number > 0:
#     print(f"{number} is positive")
# elif number < 0:
#     print(f"{number} is negative")
# else:
#     print(f"{number} is zero")
