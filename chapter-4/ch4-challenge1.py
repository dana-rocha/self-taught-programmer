#!/usr/bin/env python3

# Chapter 4 Challenge 1
# By Dana Rocha 11/24/20

# Write a function that takes a number as an input and returns that number squared

def square(x):
    """
    This function returns the square of a number thats passed in
    :param x: int
    :return: int, x squared
    """
    return(int(x**2))

sq = square(2)
print(sq)
