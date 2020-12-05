#!/usr/bin/env python3

# Exercise 5 in practicepython.org
# Dana Rocha 12/4/20


# Write a program that takes two lists and returns a list 
# That contains only the elements that are common between the lists

a = [ 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

b = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

both = []

for let in a:
   if let in b:
      both.append(let)

print(both)
