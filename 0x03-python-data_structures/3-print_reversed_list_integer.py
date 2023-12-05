#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for RevList in range(len(my_list)-1, -1, -1):
        if isinstance(my_list[RevList], int):
            print("{:d}".format(my_list[RevList]))
