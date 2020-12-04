#!/usr/bin/env python3

# Exercise 2 on practicepython.org

# Ask the user for a number
# Print out if the number is even or odd



userIN = int(input("Enter a number:"))


def test_num(x):
    if x % 2 == 0:
        print("The number is even!")
    else:
        print("It's odd!!")

test_num(userIN)
