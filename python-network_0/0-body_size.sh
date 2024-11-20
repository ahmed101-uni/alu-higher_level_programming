#!/bin/bash
# Uses curl on the first argument and prints the size of it.
curl -s "$1" | wc -c
