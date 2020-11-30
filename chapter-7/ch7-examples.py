#!/usr/bin/env python3


# Chapter 7: For loops
# By Dana Rocha 11/27/20



# For-loops are used to iterate through an iterable

name = "Ted"

for character in name:
    print(character)



# Iterating through a list

shows = ["GOT",
         "Narcos",
         "Vice"]

for show in shows:
    print(show)


# Iterating through a tuple
coms = ("A. Development",
        "Friends",
        "Always Sunny")


for show in coms:
    print(show)


# Iterating through the keys in a dictionary

people = {"G. Bluth II": "A. Development",
          "Barney": "HIMYM",
          "Dennis": "Always Sunny"}


for character in people:
    print(character)



# Using counters
# Can use for-loops to change the items in a mutable iterable like a list
tv = ["GOT",
      "Narcos",
      "Vice"]

# Using a counter and incrementing the counter in the for loop
i = 0
for show in tv:
    new = tv[i]
    new = new.upper()
    tv[i] = new
    i += 1

print(tv)


# Syntax for item and index

tv = ["GOT",
      "Narcos",
      "Vice"]

for i, show in enumerate(tv, 0):
    new = tv[i]
    new = new.upper()
    tv[i] = new

print(tv)


# changing index and printing separately
for count,ele in enumerate(tv,0):
    print(count,ele)




# Using for loops to move data between mutable iterables
tv = ["GOT",
      "Narcos",
      "Vice"]

coms = ["Arrested Development",
        "friends", "Always Sunny"]

all_shows = []


for show in tv:
    show = show.upper()
    all_shows.append(show)

for show in coms:
    show = show.upper()
    all_shows.append(show)

print(all_shows)


# Using the range function
for i in range(1, 11):
    print(i)



# While loops: executes code as long as an expression evaluates to true
x = 10
while x > 0:
    print("{}".format(x))
    x -= 1
print("Happy New Year!")




# Can use a break statement to terminate a loop
# As oon as Python hits the break-statement, the loop ends

for i in range(0, 100):
    print(i)
    break


# Using the while loop and break keyword to write a program that keeps asking the user for input
# until they type q to quit

qs = ["What is your name?",
      "What is your fave color?",
      "What is your quest?"]

n = 0

while True:
    print("Type q to quit!")
    a = input(qs[n])
    if a == "q":
        break
    n = (n + 1) % 3




# Continue statements -  stop the current iteration of a loop and move on to the next iteration of it
# print all the numbers 1 to 5 except for 3
for i in range(1, 6):
    # If i == 3, move on to the next i
    if i == 3:
        continue
    print(i)


# Can do the same thing using a while loop and a continue statement
i = 1

while i <= 5:
    if i == 3:
        i += 1
        continue
    print(i)
    i += 1


# Nested Loops
# The inner loop iterates through its iterable once for each time around the outer loop

for i in range(1, 3):
    print(i)
    for letter in ["a", "b", "c"]:
        print(letter)



# Iterating through a list with a nested for-loop
# The first loop iterates through every integer in list1
# For every variable j in the second loop, add it to the integer in list1 and append the result to added
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
added = []

for i in list1:
    for j in list2:
        added.append(i + j)

print(added)


#Nesting a for-loop inside a while-loop

while input("y or n?") != "n":
    for i in range(1, 6):
        print(i)
