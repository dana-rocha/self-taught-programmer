#!/usr/bin/env python3

# Chapter 9 Challenge 1
# By Dana Rocha 12/1/20

# Find a file on your computer and print its contents using Python

import os
mushroom_path = os.path.join("/Users", "danabridgette", "Documents", "Fall_2020", "DA5030", "mushrooms.csv")


my_mushroom = []

with open(mushroom_path, "r") as f:
    my_mushroom.append(f.read())


print(my_mushroom[0])

