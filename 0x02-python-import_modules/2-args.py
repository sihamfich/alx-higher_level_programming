#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    val = len(argv) - 1
    if val < 1:
        print("{} arguments.".format(val))
    elif val == 1:
        print("{} argument:".format(val))
    else:
        print("{} arguments:".format(val))
    for i in range(value):
        print("{}: {:s}".format(i + 1, argv[i + 1]))
