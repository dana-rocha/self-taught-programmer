#!/usr/bin/env python3

# Chapter 4 Challenge 3
# By Dana Rocha 11/24/20

# Write a function that takes three required parameters and two optional parameters

def calcu(a, d, x, y = 2, z = 3):
    """
    This function takes in 3 required parameters and two optional parameters. The function returns the sum
    of the parameters.
    :param a: int
    :param d: int
    :param x: int
    :param y: int
    :param z: int
    :return: int, sum of the parameters
    """
    return(x + y + z + a + d)

print(calcu(0, 8))
