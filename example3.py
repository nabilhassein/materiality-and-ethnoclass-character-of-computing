### PART 3: libraries, random numbers, more complex logic
import random

answer = random.randint(1, 100)
guess = 0

while guess != answer:
    guess = int(input("guess the number from 1-100 "))

    if guess < answer:
        print("your guess is too small")
    elif guess > answer:
        print("your guess is too big")
    else:
        print("you win!")

## exercises:
# Shorten or lengthen the range involved with the game.
# Modify the game so the user loses after a certain number of guesses, instead of trying forever.
# Challenge: write a rock-paper-scissors game.
  # Hint: you can use a list that looks like the next line, and pick a random element by using the line after:
  # choices = ["rock", "paper", "scissors"]
  # computer = random.choice(choices)
