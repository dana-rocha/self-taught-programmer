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

# Python raises an exception when you try to look up a character that's past the last index in your string
author[5]

# Can use negative indices
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

"Hello.Yes!".split(".")

# Splitting the string on the "."



# Join

first_three = "abc"

result = "+".join(first_three)
result

# Can turn a list of strings into a single string by calling the join method on an
# empty string and passing in the list as a parameter

words = ["The", "fox", "jumped", "over", "the", "fence", "."]

one = "".join(words)
one



# Can separate with spaces

two = " ".join(words)
two



# Strip space

s = "                The        "
s = s.strip()
s


# Replace method
# Replaces every occurrence of a string with another string

equ = "All animals are equal."
equ = equ.replace("a", "@")
print(equ)


# Find an Index
# Returns the index of the first occurrence of a character in a string

"animals".index("m")

# Raises an error because not found
"animals".index("z")

# Exception handling instead
try:
    "animals".index("z")
except:
    print("Not found.")


# In keyword checks if a string is in another string and returns a boolean
"Cat" in "Cat in the hat."

"Bat" in "Cat in the hat."


"Potter" not in "Harry"


# Escaping strings
# Python uses a backslash for escaping
# Using quotes inside of a string

# Raises a syntax error
#"She said "Surely""

# Fix the error:
"She said \"Surely.\""

'She said \"Surely.\"'

"She said 'Surely.'"

# Can put double quotes inside of single quotes
'She said "Surely."'



# Newline
print("line1\nline2\nline3")


# Slicing a list

fict = ["Tolstoy",
        "Camus",
        "Orwell",
        "Huxley",
        "Austin"]

fict[0:3]


# Slicing a string

ivan = "In place of death there was light."

ivan[0:17]

ivan[17:]

ivan[:]

ivan[::-1]


