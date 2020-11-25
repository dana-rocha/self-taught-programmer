# Chapter 3 Examples from The Self Taught Programmer
# Dana Rocha 11/20/20


# Example 1

# This is a comment
print("Hello, World!")

# Keep comments concise and use sparingly


# Example 2
import math

# Length of a diagonal
l = 4
w = 10
d = math.sqrt(l**2 + w**2)

print(d)

# Example 3
# Code surrounded by three quotes, parentheses, brackets, and braces can extend to a new line
print("""This is a really really 
really really long line of code""")


# Example 4
# Can also use a backward slash \ to extend code to the next line
print\
    ("""This is a really really
    really long line of code.""")


# Example 5
# Conditional Statements
home = "America"

if home == "America":
    print("Hello, America!")
else:
    print("Hello, world!")


# Example 6
home = "Canada"

if home == "America":
    print("Hello, America!")
else:
    print("Hello, world!")


# Example 7
home = "America"
if home == "America":
    print("Hello, America!")


# Example 8
x = 2

if x == 2:
    print("The number is 2.")
if (x % 2 == 0):
    print("The number is even.")
if (x % 2 != 0):
    print("The number is odd.")

# Example 9
# Nesting
x = 10
y = 11

if (x == 10):
    if (y == 11):
        print(x + y)


# Example 10
# Elif statements
home = "Thailand"

if home == "Japan":
    print("Hello, Japan!")
elif home == "Thailand":
    print("Hello, Thailand!")
elif home == "India":
    print("Hello, India!")
elif home == "China":
    print("Hello, China!")
else:
    print("Hello, World!")

# Example 11
home = "Mars"

if home == "America":
    print("Hello, America!")
elif home == "Canada":
    print("Hello, Canada!")
elif home == "Thailand":
    print("Hello, Thailand!")
elif home == "Mexico":
    print("Hello, Mexico!")
else:
    print("Hello, World!")

# Example 12
# Multiple if-statements and elif-statements in a row
# Three compound statements

x = 100

if x == 10:
    print("10!")
elif x == 20:
    print("20!")
else:
    print("I don't know!")


if x == 100:
    print("x is 100!")


if x % 2 == 0:
    print("x is even!")
else:
    print("x is odd!")
