#!/usr/bin/env python3

# Chapter 10: Bringing It All Together

# Hangman Game



# The computer will be Player One
# Player One picks a secret word and draws a line for each letter in it
# Player Two tries to guess the word one letter at a time
# If Player Two guesses a letter correctly, Player One replaces the corresponding underscore with the correct letter
# If Player Two guesses incorrectly, Player One draws a body part of a hanged stick figure (starting with the head)
# If Player Two completes the word before the drawing of the hangman is complete, they win. If not, they lose.


import random



def hangman():
    """
    Hangman function to store the game
    :param word: The word that Player Two has to guess
    :return: str, Welcome message
    """

    word_list = ["cat", "dog", "bunny", "python", "snake", "purple"]
    random_number = random.randint(0, 5)
    word = word_list[random_number]

    # Keep track of how many incorrect letters Player Two has guessed
    wrong = 0
    stages = ["",
              "________       ",
              "|              ",
              "|        |     ",
              "|        O     ",
              "|       /|\    ",
              "|       / \    ",
              "|              "
              ]

    # Store the characters in the word variable
    rletters = list(word)

    # Keep track of the hints displayed to Player Two
    board = ["__"] * len(word)

    # Keep track of whether Player Two has won the game
    win = False

    print("Welcome to Hangman")

    # The game keeps going as long as Player Two does not guess more wrong letters
    # than the number of strings that make up the hangman
    # Have to subtract 1 because stages list starts counting from 0 and wrong starts counting at 1
    while wrong < len(stages) - 1:
        print("\n")
        char = input("Guess a letter")

        if char in rletters:
            # If the guess is part of the word, get the index in rletters
            cind = rletters.index(char)
            # Using the index to display the guess on the board
            board[cind] = char
            # Replace the correctly guessed character with a dollar sign
            rletters[cind] = '$'
        else:
            # If Player Two guessed incorrectly, increment by 1
            wrong += 1

        print((" ".join(board)))

        # Printing the hangman at whatever stage the game is at
        # Need to add 1 because when slicing, the end slice does not get included in the result
        e = wrong + 1
        print("\n".join(stages[0:e]))

        # Check if Player Two won the game
        if "__" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break

    if not win:
        print("\n".join(stages[0:wrong]))
        print("You lose! It was {}.".format(word))

hangman()
