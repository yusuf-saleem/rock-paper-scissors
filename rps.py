import pytest
from random import randrange

moves = {1:"rock", 2:"paper", 3:"scissiors"}

def main():

    print("----------------------")
    print("Rock, Paper, Scissors!")
    print("----------------------")

    while(True):
        userInput = input("Enter move (r/p/s): ")
        userMove = getUserMove(userInput)
        if userMove in moves:
            # Valid move, accept and break loop
            break
    
    print("[You]: %s" % moves.get(userMove))
    cpMove = getCpMove()
    print("[Computer]: %s" % moves.get(cpMove))
    result = declareWinner(userMove, cpMove)
    print("You %s!" % result)

def getUserMove(userInput):

    """Returns user's move ID based on userInput text provided"""

    if userInput == "r": return 1
    elif userInput == "p": return 2
    elif userInput == "s": return 3
    else:
        print("Invalid input!")
        return -1

def getCpMove():

    """Returns the computer's move ID as specified in the 'moves dictionary"""
    return randrange(1,4)

def declareWinner(userMove, cpMove):

    """Returns either Win, Lose, or Draw based on the user's move and the computer's move"""

    if userMove not in moves:
        return "InputError"
    if cpMove not in moves:
        return "InputError"
    if userMove == cpMove:
        return "Draw"
        
    if userMove == 1:
        if cpMove == 2:
            return "Lose"
        elif cpMove == 3:
            return "Win"

    if userMove == 2:
        if cpMove == 1:
            return "Win"
        elif cpMove == 3:
            return "Lose"
        
    if userMove == 3:
        if cpMove == 1:
            return "Lose"
        elif cpMove == 2:
            return "Win"

    return "ImpossibleStateError"

if __name__ == "__main__":
    main()