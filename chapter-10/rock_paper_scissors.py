#!/usr/bin/env python3

# Exercise 8 from practicepython.org
# Dana Rocha 1/4/21

# Make a two-player Rock-Paper-Scissors game
# Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner,
# and ask if the players want to start a new game
import sys

player1 = input("Player 1: Do you want to choose rock, paper, or scissors?").lower()
player2 = input("Player 2: Do you want to choose rock, paper, or scissors?").lower()


def play_game(p1, p2):

    if p1 == p2:
        return("It's a tie!")
    elif p1 == "rock":
        if p2 == "scissors":
            return("Player 1 wins!")
        else:
            return("Player 2 wins!")
    elif p1 == "scissors":
        if p2 == "paper":
            return("Player 1 wins!")
        else:
            return("Player 2 wins!")
    elif p1 == "paper":
        if p2 == "rock":
            return("Player 1 wins!")
        else:
            return("Player 2 wins!")
    else:
        return("Try again! You have to enter: rock, paper, or scissors to play")
        sys.exit()

print(play_game(player1, player2))
