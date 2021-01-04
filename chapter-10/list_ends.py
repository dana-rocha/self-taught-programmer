#!/usr/bin/env python3

# Exercise 12 from practicepython.org
# Dana Rocha 1/3/21

# Write a program that takes a list of numbers and makes a new list
# and makes a new list of only the first and last elements of the given list.
# For practice, write this code inside a function.

a = [5, 10, 15, 20, 25]

def list_ends(l):
    b = [l[0], l[len(l)-1]]
    return b

print(list_ends(a))
