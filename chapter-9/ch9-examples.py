#!/usr/bin/env python3

# Chapter 9 Challenges
# By Dana Rocha 11/30/20


# Create file paths using the os module to avoid problems with working across different operating systems
import os
os.path.join("Users","bob", "st.txt")


# Must close the file if you open a file using the open method
st = open("st.txt", "w")
st.write("Hi from Python!")
st.close()

# with statement automatically closes the file
with open("st.txt", "w") as f:
    f.write("Hi from Python!")


# Reading from files
# You can only read on a file once, so should save the file contents in a variable or container

my_list = list()

with open("st.txt", "r") as f:
    my_list.append(f.read())

print(my_list)


# Writing csv files

import csv

with open("st.csv", "w", newline="") as f:
    w = csv.writer(f, delimiter=",")
    w.writerow(["one", "two", "three"])
    w.writerow(["four", "five", "six"])


# Reading csv files
# Opening st.csv for reading and convert to a csv object using the reader method 
import csv

with open("st.csv", "r") as f:
    r = csv.reader(f, delimiter=",")
    for row in r:
        print(",".join(row))
