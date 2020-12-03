#!/usr/bin/env python3


# Dice Rolling Simulator

import random

min_int = 1
max_int = 6

repeat = True

while repeat:
    print("You rolled", random.randint(min_int, max_int))

    userIN = input("Do you want to roll again? Y/N").upper()

    if userIN == "N":
        repeat = False
    else:
        continue

