#Importing the random module
import random

#Var that stores random number from 1 to 100
number = random.randint(1,100)

#Initilize the guess var to be 0
guess = 0

#Loop until the guess is not equal to number
while guess != number:

    #prompt the user to input their guess
    guess=int(input("Enter the guess number: "))

    #If the guess is higher then random number let user know the guess is higher
    if (guess > number):
        print("Too High!")

    #If the guess is lower then random number let user know the guess is lower 
    elif (guess < number):
        print("Too Low!")
    
    #If guess is equal to random number user wins;
    else:
        print("You Won!")