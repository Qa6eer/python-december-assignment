import random

def guess_game():
    number = random.randint(1, 50)
    print("I'm thinking of a number between 1 and 50. Can you guess it?")
    
    while True:
        try:
            guess = int(input("Guess a number: "))
            if guess == number:
                print("Correct! You guessed it!")
                break
            elif guess < number:
                print("Too low, try again.")
            else:
                print("Too high, try again.")
        except ValueError:
            print("Invalid input. Please enter an integer.")