#!/bin/bash
# Sends request with an added custom header
curl -s -H "X-School-User-Id: 98" "$1"
