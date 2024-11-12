#!/usr/bin/python3
"""
This module provides a function to load data from a JSON file.
"""
import json


def load_from_json_file(filename):
    """
    Load data from a JSON file and return it as a Python object.
    """

    with open(filename, "r", encoding="utf-8") as f:
        jsonObj = f.read()
        return json.loads(jsonObj)
