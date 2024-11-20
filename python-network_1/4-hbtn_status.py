#!/usr/bin/python3
"""
    This script makes a request and displays a
    response using the requests package.
"""

import requests

if __name__ == "__main__":
    response = requests.get("https://alu-intranet.hbtn.io/status")

    print("Body response:")
    print(f"\t- type: {type(response.text)}")
    print(f"\t- content: {response.text}")
