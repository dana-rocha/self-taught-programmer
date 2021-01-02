#!/usr/bin/env python3

# Exercise 7 from practicepython.org
# Dana Rocha 1/1/21

# Given a list, write one line of Python that takes this list and makes a new list that has only the even elements in it

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Long way
for i in a:
    if i % 2 == 0:
        print(i)


# Using list comprehension
b = [x for x in a if x % 2 == 0]

print(b)
