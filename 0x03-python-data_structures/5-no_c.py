#!/usr/bin/python3

def no_c(my_string):
    new_str = ''
    for _string in my_string:
        if _string != 'c' and _string != 'C':
            new_str += _string
        return (new_str)
