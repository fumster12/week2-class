import random

number_in_my_head = random.randint(1, 100)

print("I'm thinking of a number between 1 and 100.")

guess = eval(input("Can you guess it? "))

# CHALLENGE:
#
# The user gets one guess.
#
# If the guess matches the number_in_my_head,
# tell the user that they won the game.
#
# Otherwise, display a message telling them whether
# the number was higher or lower.
