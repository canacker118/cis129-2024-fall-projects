'''
    Script: DiceGame.py
    Action: a.Has the two players input their names
            b.Randomly generates a number from 1 to 6 for wach player
            c.Declares a winner based on the higher number, or a tie if the numbers are the same
    Author: Chris Anacker
    Date: 10/27/2024
'''
import random

def inputNames():
    '''
    Action: Prompts the users to enter their names

    Input: The user is propmted to input names
    Output: Displays prompt for player 1 and player 2
    Return: none
    '''
    player1 = input("Enter Player 1 name: ") #Player 1 enters their name
    player2 = input("Enter Player 2 name: ") #Player 2 enters their name
    return player1, player2

def rollDice():
    '''
    Action: Two random numbers are generated form 1 to 6 as if the user is roling two six-sided dice

    Input: None
    Output: None
    Return: None
    '''
    dice1 = random.randint(1, 6) #Roll dice 1
    dice2 = random.randint(1, 6) #Roll dice 2
    return dice1, dice2

def displayInfo(player1, player2, score1, score2):
    '''
    Action: Compares the scores of the two players and prints the winner or a tie message

    Input: a. player1: Name of Player 1
           b. player2: Name of Player 2
           c. score1: Score of Player 1
           d. score2  Score of Player 2
    Output: Message indicating the winner or if the game is a tie
    Return: None
    '''
    if score1 > score2:
        print(player1, "wins!") # Player 1 has the higher number on the dice roll
    elif score1 < score2:
        print(player2, "wins!") # Player 2 has the higher number on the dice roll
    else:
        print("It's a tie!") # Both numbers rolled are equal

def main():
    '''
    Action: Controls the game's functions until the user chooses to end the program

    Input: a. Input Player 1 and Player 2 name
           b. Input response to end the program
    Output: a. Displays the winner or tie
            b. Prompts the user if they want to play again
    Return: None 
    '''
    print()

    endProgram = 'no' #Causes the game to loop back and start again
    player1, player2 = "", "" 
    score1, score2 = 0, 0 # Initializes the score for both players

    player1, player2 = inputNames() #Input prompts for the player's name

    while endProgram == 'no': #Program continues to run until the user ends it

        dice1, dice2 = rollDice() #Dice roll for both players
        score1 += dice1 #Dice 1 score
        score2 += dice2 #Dice 2 score

        displayInfo(player1, player2, score1, score2) #Display current standing

        endProgram = input('Do you want to end program? (yes/no): ') #Prompt to end the program

main()
