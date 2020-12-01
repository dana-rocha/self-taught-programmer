#!/usr/bin/env python3

# Checking if vowel or consonant
# Dana Rocha 12/1/20


# The user is asked to input a character
# The program checks whether the entered character is a vowel or not


vowels = ["a", "e", "i", "o", "u"]

userIN = input("Please input a letter:").lower()

if userIN in vowels:
    print("It's a vowel!")
else:
    print("It's a consonant!")
