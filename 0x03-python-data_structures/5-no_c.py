#!/usr/bin/python3
def no_c(my_string):
    result = ""
    for _string in my_string:
        if _string.lower() != 'c':
            result += _string
    return result
