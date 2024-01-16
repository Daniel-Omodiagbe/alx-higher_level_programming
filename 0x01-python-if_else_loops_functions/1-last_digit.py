#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    numb = number % 10
    if numb > 5:
        print(f"Last digit of {number} is {numb} and is greater than 5")
    elif numb == 0:
        print(f"Last digit of {number} is {numb} and is 0")
    else:
        print(f"Last digit of {number} is {numb}\
            and is less than 6 and 6 and not 0")
elif number < 0:
    number = number * -1
    numb = number % 10
    print(f"Last digit of {number * -1} is {numb * -1}\
        and is less than 6 and not 0")
