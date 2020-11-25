#!/usr/bin/env python3

# Chapter 4 Challege 4
# By Dana Rocha 11/24/20


# Write a program with two functions.
# The first function should take an integer as a parameter and return the result of the integer divided by 2
# The second function should take an integer as a parameter and return the result of the integer multiplied by 4
# Call the first function, save the result as a variable, and pass it as a parameter to the second function


def return_int(x):
    """
    This function takes in an integer and returns the result of the integer divided by 2
    :param x: int
    :return: int, x /2
    """
    try:
        return(int(x / 2))
    except ValueError:
        print("Invalid Input!!")

def multi_4(z):
    """
    This function takes in an integer and returns the result of the integer multiplied by 4
    :param z: int
    :return: int, x * 4
    """
    try:
        return(int(z * 4))
    except ValueError:
        print("Can't! Need an integer!")

nums = return_int(24)
print(multi_4(nums))
