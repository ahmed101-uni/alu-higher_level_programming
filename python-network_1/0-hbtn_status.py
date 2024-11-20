#!/usr/bin/python3
"""
This script fetches the status from a given URL using the urllib library.
"""

import urllib.request

if __name__ == "__main__":
    url = "https://alu-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as request:
        print("Body response:")
        data = request.read()
        print("\t- type: {}".format(type(data)))
        print("\t- content: {}".format(data))
        print("\t- utf8 content: {}".format(data.decode("utf-8")))
