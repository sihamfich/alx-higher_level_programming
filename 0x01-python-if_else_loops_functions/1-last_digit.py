#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
_str = "Last digit of{: } is{: } and is".format(number, last_digit)
if last_digit < 6 and last_digit != 0:
    print(str(_str), "less than 6 and not 0")
elif last_digit == 0:
    print(str(_str), "0")
else:
    print(str(_str), "greater than 5")
