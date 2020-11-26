#!/usr/bin/env python3

# Chapter 5 Tuple Examples
# By Dana Rocha 11/24/20

# Tuple is a container that stores objects in a specific order
# Tuples are immutable - the contents cannot change once its made
# Tuples are represented by parentheses

my_tuple = tuple()
my_tuple


rndm = ("M. Jackson", 1958, True)
rndm

# Even if a tuple only has one item in it, you need to put a comma after it
("self_taught", )

# You can't add new items to a tuple or change it once its been created
# Python will raise an exception

dys = ("1984", "Brave New World", "Fahrenheit 451")

dys[1] = "Handmaid's Tale"

# Index and check an item
dys[2]

"1984" in dys

# Tuples (unlike lists) can be used as keys in dictionaries
