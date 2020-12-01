#!/usr/bin/env python3

# Chapter 8: Modules
# By Dana Rocha 11/30/20

import math
print(math.pow(2,3))


import random
print(random.randint(0, 100))


import statistics

# Mean
nums = [1, 5, 33, 12, 46, 33, 2]
statistics.mean(nums)

# Median
statistics.median(nums)

# Mode
statistics.mode(nums)


import keyword
keyword.iskeyword("for")

keyword.iskeyword("football")


