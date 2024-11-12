#!/usr/bin/python3
"""
This module provides a script to add command line
arguments to a list stored in a JSON file.
"""
import sys
import importlib

load_from_json_file = importlib.import_module(
    "6-load_from_json_file"
).load_from_json_file
save_to_json_file = importlib.import_module(
    "5-save_to_json_file"
).save_to_json_file


def add_item():
    """
    Adds command-line arguments to a list stored in a JSON file.
    """
    try:
        arr = load_from_json_file("add_item.json")
    except Exception:
        arr = []
    arr += sys.argv[1:]

    save_to_json_file(arr, "add_item.json")


add_item()
