#!/usr/bin/env python3

# Exercise 3 from practicepython.org
# Dana Rocha 12/3/20


# Take a list and write a program that prints out all the elements of the list that are less than 10
# Extra: Instead of printing the elements one by one, make a new list that has all the elements less than 10


a = [1,1,2,3,5,8,13,21,24,34,55,89]
new_list = []

for num in a:
    if num < 10:
        new_list.append(a)

print(new_list)
