#!/bin/bash
# check if the status code is 200, then print the body of the request if so.
curl -sL -w "%{http_code}" "$1" -o /dev/null | grep -q "200" && curl -sL "$1"
