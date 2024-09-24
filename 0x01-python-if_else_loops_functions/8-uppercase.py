#!/usr/bin/python3
def uppercase(str):
    for x in str:
        if 97 <= ord(x) <= 122:
            print('{}'.format(chr((ord(x)) - 32)), end="")

        else:
            print('{}'.format(x), end="")

        print()
