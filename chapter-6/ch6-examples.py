#!/usr/bin/env python3

# Chapter 6: String Manupulation
# By Dana Rocha 11/26/20



# Triple Strings
# If a string spans more than one line, you have to put it in triple quotes:

"""
    line one
    line two
    line three
"""


# Indexes

# Strings, lists, tuples are iterable
# You can look up each character in a string with an index


author = "Kakfa"

author[0]
author[1]
author[2]
author[3]
author[4]

# Python raises an exception when you try to look up a character thats past the last index in your string
author[5]

# Can use negative indeces
author[-1]

author[-3]



# Strings are immutable. You can't change the characters in a string. To change the characters in a string,
# you have to create a new string
ff = "F. Fitzgerald"
ff = "F. Scott FItzgerald"
ff


# Concatenation
"cat" + "in" + "hat"

"cat" + " in" + " the" + " hat"


# String Manipulation
"Sawyer" * 3


# Changing Case

# Change all letters to uppercase
"We hold these truths...".upper()

# Change all letters to lowercase
"SO IT GOES...".lower()

# Capitalize the first letter of a sentence
"four score and...".capitalize()



# Format
# You can create a new string using the format method, which looks for occurrences of curly brackets

"William {}".format("Faulkner")

# Can pass in a variable
last = 'Faulkner'

"William {}".format(last)

# Can use multiple curly brackets
author = "William Faulkner"
year_born = "1897"

"{} was born in {}.".format(author, year_born)



# Format method is useful if you are creating a string from user input
n1 = input("Enter a noun:")
v = input("Enter a verb:")
adj = input("Enter an adj:")
n2 = input("Enter a noun:")

r = """The {} {} the {} {}
    """.format(n1, v, adj, n2)

print(r)


# Split
# Strings have a method called split. You can separate one string into two or more strings.



