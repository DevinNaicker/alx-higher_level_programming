#!/usr/bin/python3
str = "apple98 is coming TODAY"
for x in str:
    if 97 <= ord(x) <= 122:
        print('{}'.format(chr((ord(x)) - 32)), end="")
