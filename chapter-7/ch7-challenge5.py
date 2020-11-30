#!/usr/bin/env python3


# Chapter 7 Challenge 5

# Multiply all the numbers in the list [8, 19, 148, 4] with all the numbers in the list [9, 1, 33, 83]
# and append each result to a third list


list1 = [8, 19, 148, 4]
list2 = [9, 1, 33, 83]

multi = []

for i in list1:
    for j in list2:
        multi.append(i * j)

print(multi)
