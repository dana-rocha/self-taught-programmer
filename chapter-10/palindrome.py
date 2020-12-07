#!/usr/bin/env python3

# Exercise 6 from practicepython.org
# Dana Rocha 12/6/20

# Ask the user for a string and print out whether this string is a palindrome or
# not

userIN = input("Enter a string:")

test = userIN[::-1]

if test == userIN:
   print("It's a palindrome!")
else:
   print("Nope")


