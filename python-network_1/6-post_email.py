#!/usr/bin/python3
"""
This script makes a post request with the requests package
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    data = {"email": sys.argv[2]}
    response = requests.post(url, data=data)

    print(response.text)
