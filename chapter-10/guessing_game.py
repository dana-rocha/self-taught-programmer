#!/usr/bin/env python3

# Exercise 9 from practicepython.org
# Dana Rocha 1/5/21

# Generate a random number between 1 and 9 (including 1 and 9). Ask the use to guess the number, then tell them
# whether they guessed two low, two high, or exactly right.

# Keep the game going until the use types "exit"
# Keep track of how many guesses the use has taken, and when the game ends, print this out.

import random

a = random.randint(1, 9)

user_in = 0
counter = 0


while user_in != "exit" and user_in != a:

    user_in = input("Guess the number!")

    if user_in == "exit":
        break

    user_in = int(user_in)
    counter += 1

    if user_in > a:
        print("Your guess is too high.")
    elif user_in < a:
        print("Your guess is too low.")
    elif user_in == a:
        print("You guessed correctly! It took you", counter, "tries!")
