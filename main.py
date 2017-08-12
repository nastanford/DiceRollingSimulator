def header():
    print("********************************")
    print("***  Dice Rolling Simulator  ***")
    print("***   By Nathan Stanford Sr  ***")
    print("********************************\n")


# Set the default values of the Dice
Dice1Start = 1
Dice1End = 6
EndGame = 'n'
import random

header()

while EndGame =="n":
    continueGame = input("Do you want to roll the dice? ")
    if(continueGame == 'n'):
        EndGame = 'y'
    print(random.randint(Dice1Start,Dice1End))



