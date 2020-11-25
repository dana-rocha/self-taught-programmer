#!/usr/bin/python

# Chapter 4 Challenge 5
# By Dana Rocha 11/24/20

# Write a function that converts a string to a float and returns the result
# Use exception handling to catch the except that could occur

def convert_string(x):
    try:
        return(float(x))
    except ValueError:
        print("Cannot convert string to float")


convert_string("Twenty -five")

convert_string(25)
