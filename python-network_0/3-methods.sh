#!/bin/bash
# print all allowed methods
curl -i -sL -X OPTIONS "$1" | grep "Allow" | cut -f2 -d":" | tail -c +2
