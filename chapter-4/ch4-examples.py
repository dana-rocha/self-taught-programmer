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
# A function does not have to include a return statement
# If a function doesn't have a return statement, it returns None

def f():
    z = 1 + 1

result = f()
print(result)


# Built-in Functions

# Returns the length of an object
len("Monty")

len("Python")

# Takes an object and returns a new object with str data type
str("100")

# Takes an object and returns an integer object
int("1")

# Takes an object and returns a floating-point number object
float(100)


# Any error that isn't a syntax error is an exception

# Collects info from the person using the program
age = input("Enter your age:")
int_age = int(age)

if int_age < 21:
    print("You are young!")
else:
    print("Wow you are old!")


# Reusing Functions
# Functions can encapsulate functionality you want to reuse
# Functions allow you to write less code because you can reuse functionality

def even_odd(x):
    if x % 2 == 0:
        print("even")
    else:
        print("odd")

even_odd(2)
even_odd(3)

# Instead of asking the user to enter a number three times, put it in a function and call the function 3 times

def even_odd():
    n = input("type a number:")
    n = int(n)
    if n % 2 == 0:
        print("n is even")
    else:
        print("n is odd")

even_odd()
even_odd()
even_odd()


# Optional Parameter
# if the optional parameter is not passed in, the function will use its default value instead

def f(x = 2):
    return x ** x

print(f()) # Using the default parameter
print(f(4))

# You can have a function that has both required and optional parameters
# The required parameters must be defined before the optional ones

def add_it(x, y = 10):
    return x + y

result = add_it(2)
print(result)



# Scope
# Variables have scope
# Scope refers to what part of the program can read and write to it

# A variable defined outside of a function or class has a global scope
# it can be read or written to from anywhere in the program

# A variable defined inside of a function or class has local scope
# The program can only read or write to it in the function or class the variable was defined in

# Global Scope
x = 1
y = 2
z = 3

def f():
    print(x)
    print(y)
    print(z)

f()
