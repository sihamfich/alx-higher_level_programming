#!/usr/bin/python3
def uppercase(str):
    for element in str:
        if ord(element) >= 97 and ord(element) <= 122:
            i = chr(ord(element) - 32)
        print("{}".format(element), end="")
    print()
