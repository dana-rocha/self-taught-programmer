#!/usr/bin/env python3

# Chapter 9 Challenge 2
# By Dana Rocha 12/1/20


userIN = input("What is your favorite color:")


with open("color.txt", "w") as f:
    f.write(userIN)
