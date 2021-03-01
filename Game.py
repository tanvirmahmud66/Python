from random import randint

for x in range(1,6):
    guessNumber = int(input("Enter a number from 1 to 5: "))
    randomNumber = randint(1, 5)

    if guessNumber == randomNumber:
        print("You Won The Game :) ")
    else:
        print(f"You loss :( !! The Random Number was: {randomNumber}")
