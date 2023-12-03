#!/usr/bin/python3
import random
number = random.randint(-10000, 10000))
last_digit = abs(number) % 10
print("Last digit of {} is {} and is".format(number, last_digit))
if last_digit < 6 and last_digit != 0:
    print("less than 6 and not 0")
elif last_digit == 0:
    print("0")
else:
    print("greater than 5"))
