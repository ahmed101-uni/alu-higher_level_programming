#!/usr/bin/python3
"""
This script makes a request and displays a header variable.
"""
import requests
import sys

if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    try:
        print(response.headers["X-Request-Id"])
    except KeyError:
        print("None")
