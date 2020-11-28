#!/usr/bin/env python3

# Chapter 6 Challenge 2
# By Dana Rocha 11/27/20


# Write a program that collects two strings from a user, inserts them into the string and prints a new string


userIN = input("Enter an form of communication (book, letter, text, etc): ")
userSent = input("Enter a name!")

print("Yesterday I wrote a {}. I sent it to {}!".format(userIN, userSent))
