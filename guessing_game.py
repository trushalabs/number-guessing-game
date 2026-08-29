import random

while True:
    print("==============================")
    print("     NUMBER GUESSING GAME")
    print("==============================")
    print("I have chosen a number between 1 and 100.")
    print("Try to guess it!")
    print()

    number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts = attempts + 1

            if guess > number:
                print("Too high! Try again.")

            elif guess < number:
                print("Too low! Try again.")

            else:
                print("Congratulations! You guessed it!")
                print("You guessed the number in", attempts, "attempts.")
                break

        except ValueError:
            print("Please enter a valid number.")

    play_again = input("Do you want to play again? (yes/no): ")

    if play_again.lower() != "yes":
        print("Thanks for playing!")
        break
