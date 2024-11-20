#!/usr/bin/python3
"""
This script makes request and handles json response
"""
import requests
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    data = {"q": sys.argv[1] if len(sys.argv) == 2 else ""}
    response = requests.post(url, data=data)
    try:
        json_response = response.json()
        if not json_response:
            print("No result")
        else:
            print("[{}] {}".format(json_response["id"], json_response["name"]))
    except Exception:
        print("Not a valid JSON")
