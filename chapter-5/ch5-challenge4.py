#!/usr/bin/env python3

# Chapter 5 Challenge 4
# By Dana Rocha 11/26/20

# Write a program that lets the user ask your height, favorite color, or favorite author, and
# returns the result from the dictionary you created in the previous challenge


about_me = {"Height": "5' 1", "Fave Color": "Blue", "Fave Author": "Taylor Jenkins Reid"}

about_me


userIN = input("Ask my Height, Favorite Color, or Favorite Author:")

if userIN in about_me:
    result = about_me[userIN]
    print(result)
