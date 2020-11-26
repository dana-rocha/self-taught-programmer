#!/usr/bin/env python3

# Chapter 5: Lists
# By Dana Rocha 11/24/20



# Methods

"Hello".upper()

"Hello".replace("o", "@")




# Lists = a containers that store objects in a specific order
# Lists are represented by square brackets



# Can create an empty list with the list function
fruit = list()
fruit

# Can create a list with square brackets
[]

# Can create a list with items
fruit = ["Apple", "Orange", "Pear"]
fruit

# Add a new item to the end of the list with the append method
fruit.append("Banana")
fruit.append("Peach")


# Lists can store any data type
random = []
random.append(True)
random.append(100)
random.append(1.1)
random.append("Hello")
random


# Strings, lists, tuples are iterable

fruit = ["Apple", "Orange", "Pear"]
fruit[0]
fruit[1]
fruit[2]


# Lists are mutable - you can change, add, remove items in the list

colors = ["blue", "green", "yellow"]
colors
colors[2] = "red"
colors

# You can remove the last item from a list using the pop method

colors = ["blue", "green", "yellow"]
colors

item = colors.pop()
colors
item


# You can combine two lists

colors1 = ["blue", "green", "yellow"]
colors2 = ["orange", "pink", "black"]
colors1 + colors2


# Can check if an item is in the list with the "in" keyword

colors = ["blue", "green", "yellow"]
"green" in colors


# Can use the "not" keyword to check if an item is not in the list
colors = ["blue", "green", "yellow"]
"black" not in colors


# Size of the list
len(colors)


# Example of using a list

colors = ["purple","orange","green"]

guess = input("Guess a color:")

if guess in colors:
    print("You guessed correctly!")
else:
    print("Wrong! Try again.")
