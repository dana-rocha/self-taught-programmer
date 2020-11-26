#!/usr/bin/env python3

# Chapter 5: Dictionaries
# By Dana Rocha 11/24/20

# Key-value pairs
# Keys are mapped to values
# Dictionaries are mutable and do not store objects in a specific order
# Dictionaries are represented with curly brackets


my_dict = dict()
my_dict

my_dict = {}

my_dict


fruits = {"Apple": "Red", "Banana": "Yellow"}
fruits

# Dictionaries are unordered!



# Adding key-value pairs to a dictionary
# Keys must be immutable - a string or tuple can be a dictionary key but a list or dictionary cannot
facts = dict()

# Add a value
facts["code"] = "fun"
# Look up a key
facts["code"]

# Add a value
facts["Bill"] = "Gates"
# Look up a key
facts["Bill"]

# Add a value
facts["founded"] = 1776
# Look up a key
facts["founded"]

# Can use the "in" keyword
bill = {"Bill Gates": "charitable"}

"Bill Gates" in bill


