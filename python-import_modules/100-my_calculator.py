#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv
if __name__ == "__main__":
    args = argv
    if len(args) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    if args[2] not in ["+", "-", "*", "/"]:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a = int(args[1])
    b = int(args[3])

    if args[2] == "+":
        print("{} {} {} = {}".format(a, args[2], b, add(a, b)))
    elif args[2] == "-":
        print("{} {} {} = {}".format(a, args[2], b, sub(a, b)))
    elif args[2] == "*":
        print("{} {} {} = {}".format(a, args[2], b, mul(a, b)))
    elif args[2] == "/":
        print("{} {} {} = {}".format(a, args[2], b, div(a, b)))
