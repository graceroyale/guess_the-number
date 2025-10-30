# This following is a number guessing game that enables the user to keep guessing until they get it right

import random
guess = None
number = random.randint(1, 10)
while guess != number:
    guess = int(input("Guess a number: "))
    if guess < number:
            print ("Number is too low to be correct. Please try again.")
    elif guess > number:
            print ("Number is too high to be correct. Please try again.")
    elif guess == number:
            print ("Bravo! You got it right!")
            break
    else:
            print ("Invalid input. Please enter a number between 1 and 10.")
