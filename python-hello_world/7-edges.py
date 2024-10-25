#!/usr/bin/python3
word = "Holberton"
# why does it need to be 8 lines? To give space to use variables. Still not doing it the "intended way", screw you pep8
[first, last, middle] = [word[:3], word[-2:], word[1:-1]]

print(f"First 3 letters: {first}")
print(f"Last 2 letters: {last}")
print(f"Middle word: {middle}")
