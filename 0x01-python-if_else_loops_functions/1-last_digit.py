#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
s = "Last digit of{: } is{: } and is".format(number, last_digit)
if last_digit < 6 and last_digit != 0:
    print(f"{s: } less than 6 and not 0")
elif last_digit > 5:
    print(f"{s:} greater than 5")
else:
    print(f"{s:} 0")
