#!/usr/bin/python3
"""
This script makes request to GitHub api
"""
import requests
import sys

if __name__ == "__main__":
    url = "https://api.github.com/users/{}".format(sys.argv[1])
    token = sys.argv[2] if len(sys.argv) == 3 else ""
    headers = {"Authorization": "token {}".format(token)}

    response = requests.get(url, headers=headers)
    json = response.json()
    print(json["id"] if response.status_code < 400 else "None")
