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

# Check if key is in dictionary
"Bill Gates" in bill

# Check if key is not in dictionary
"Bill Doors" not in bill


# Deleting key-value pairs

books = {"Dracula": "Stoker", "1984": "Orwell", "The Trial": "Kafka"}

del books["The Trial"]

books

# Example using a dictionary
rhymes = {"1": "fun", "2": "blue", "3": "me", "4": "floor", "5": "live"}

n = input("Type a number:")

if n in rhymes:
    rhyme = rhymes[n]
    print(rhyme)
else:
    print("Not found.")



# Nested Containers 1
lists = []

rap = ["Kanye West", "Jay Z", "Eminem", "Nas"]

rock = ["Bob Dylan", "The Beatles", "Led Zepplin"]

djs = ["Zeds Dead", "Tiesto"]

lists.append(rap)
lists.append(rock)
lists.append(djs)

print(lists)


rap = lists[0]
print(rap)

rap.append("Kendrick Lamar")

print(rap)
print(lists)

# You can store a tuple inside a list, a list inside a tuple, and a dictionary inside of a list or tuple

# Nested Containers 2
locations = []

la = (34.0522, 188.2437)
chicago = (41.8771, 87.6298)

locations.append(la)
locations.append(chicago)

# A list of tuples
print(locations)


# Nested Containers 3
eights = ["Edgar Allan Poe", "Charles Dickens"]

nines = ["Hemingway", "Fitzgerald", "Orwell"]

# A tuple of lists
authors = (eights, nines)
print(authors)


# Nested Containers 4
bday = {"Hemingway": "7.21.1899", "Fitzgerald": '9.24.1896'}

# A tuple of dictionaries
my_list = [bday]
print(my_list)

my_tuple = [bday]
print(my_tuple)


# A list, tuple, or dictionary can be a value in a dictionary
ny = {"location": (40.7128, 74.0059), "celebs": ["W. Allen", "Jay Z", "K. Bacon"], "facts": {"state": "NY", "country": "America"}}
