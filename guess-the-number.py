import random
guess = None
number = random.randint(1, 10)
print(Welcome to the Guess the Number Game!")
while guess != number:
    guess = int(input("Guess a number: "))
    if guess < number:
            print("Number is too low to be correct. Please try again.")
    elif guess > number:
            print("Number is too high to be correct. Please try again.")
    elif guess == number:
            print("Bravo! You got it right🎉!")
            break
    else:
            print("Invalid input. Please enter a number between 1 and 10.")
        if attempts == 3:
            if number % 2 == 0:
                print("Hint: The numebr is even!")
            else:
                print("Hint: The numebr is odd!")
