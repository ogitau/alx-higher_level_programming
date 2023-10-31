#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ld = ("last digit of ")
if number >= 0:
    last = number % 10
if number < 0:
    last = number % -10
if last > 5:
    print(f"{ld}{number} is {last} and is greater than 5")
elif last == 0:
    print(f"{ld}{number} is {last} and is zero")
else:
    print(f"{ld}{number} is {last} is less than 6 and is not 0")
