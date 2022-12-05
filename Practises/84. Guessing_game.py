import random
import time

# Counts the time the player needs to finish the game.
# The player needs to guess the correct number from 1-100

# set the initial parameters
answer = random.randint(1, 100)
guess = 0

# the game starts:

guess = int(input("Please guess the correct number from 1-100: "))
# take the time
start = time.time()
while guess != answer:
    if guess > answer:
        guess = int(input("It is greater than the answer! Please guess again: "))
    elif guess < answer:
        guess = int(input("It is smaller than the answer! Please guess again: "))
end = time.time()

# get the difference:
# `end-start` will give the time in seconds
print(f"You spent {end-start:.0f} seconds to get the correct answer!")

