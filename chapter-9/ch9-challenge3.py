#!/usr/bin/env python3


# Chapter 9 Challenge 3
# By Dana Rocha 12/1/20

# Take the items in this list of lists and write them to a CSV file
# The data from each list should be a row in the file with each item in the list separated by a comma

import csv

movie_list = [["Top Gun", "Risky Business", "Minority Report"], ["Titanic", "The Revenant", "Inception"], ["Training Day", "Man on Fire", "Flight"]]


with open("movies.csv", "w", newline="") as f:
    m = csv.writer(f, delimiter=",")

    for list in movie_list:
        m.writerow(list)
