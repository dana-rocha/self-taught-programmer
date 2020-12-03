#!/usr/bin/env python3

# Exercise 1 from practicepython.org

# Create a program that asks the user to enter their name and their age
# Print out a message addressed to them that tells them the year they will turn 100 years old

user_name = input("Please enter your name:")
user_age = int(input("Please enter your age:"))

one_hundred = str((2020 - user_age) + 100)

print("You will be 100 years old in " + one_hundred)
