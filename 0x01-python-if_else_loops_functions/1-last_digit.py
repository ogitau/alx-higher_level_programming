#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ld = ("last digit of ")
if number >= 0:
    last = number % 10
if number < 0:
    last = number % -10
if last > 5:
    print("{}{} is {} and is greater than 5".format(ld, number, last)
            elif last == 0:
            print("{}{} is {} and is zero".format(ld, number, last)
                else:
                print("{}{} is {} is less than 6 and is not 0".format(ld, number, last))
