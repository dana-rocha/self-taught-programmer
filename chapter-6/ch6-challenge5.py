#!/usr/bin/env python3

# Chapter 6 Challenge 5
# By Dana Rocha 11/27/20


# Take the list and return a grammatically correct string.
# There should be a space between each word but no space between the word fence and the period


lst = ["The", "fox", "jumped", "over", "the", "fence", "."]

lst_join = " ".join(lst)

lst_join = lst_join[0:-2] + '.'
print(lst_join)
