# Chapter 4 - Functions
# Examples from The Self Taught Programmer
# 11/21/20

# Functions should only do one thing

# python convention: never use capital letters in a function name and words should be separated by underscores

# Example 1
def f(x):
    return x + 2

# Save the function's output in a variable and pass it to the print function
result = f(2)
print(result)


# Example 2
# Save the result your function returns in a variable whenever you need to use the value later

def f(x):
    return x + 1

z = f(4)

if z == 5:
    print("z is 5")
else:
    print("z is not 5")



# Example 3

# A function can have one parameter, multiple, or no parameters

def f():
    return 1+1

result = f()
print(result)


# Example 4

def f(x, y, z):
    return x + y + z

result = f(1, 2, 3)
print(result)

# Example 5
















