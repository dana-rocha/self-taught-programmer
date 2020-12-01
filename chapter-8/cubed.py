#!/usr/bin/env python3


# Chapter 8 Challenge 2

# Create a module named cubed with a function that takes a number as a parameter and returns the number cubed

def cube_it(x):
    try:
        x = int(x)
        print(x**3)
    except TypeError:
        print("Must be a number")
