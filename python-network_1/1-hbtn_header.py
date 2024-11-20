#!/usr/bin/python3
"""
This script prints the headers of the response
"""
import sys

import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.getheader("X-Request-Id"))
