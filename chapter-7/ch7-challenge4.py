#!/usr/bin/env python3


# Chapter 7 Challenge 4
# By Dana Rocha 11/29/20

# Write a program with an infinite loop (with the option to type q to quit) and a list of numbers
# Each time through the loop ask the user to guess a number on the list and tell them whether or not they guessed correctly



nums = [1, 2, 3, 4, 2456, 4756, 43, 16, 17, 8, 465, 100]



while True:
    d = input("Guess a number or type q to quit!")

    if d == "q":
        break

    try:
        d = int(d)
    except ValueError:
        print("Please type in a number or q to quit")


    if d in nums:
        print("Guessed Correctly!")
    else:
        print("Guess Again!")
