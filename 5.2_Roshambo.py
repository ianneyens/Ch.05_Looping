"""
ROSHAMBO PROGRAM
----------------

Create a program that randomly prints 1, 2, or 3.
Expand the program so it randomly prints rock, paper, or scissors using if statements. Don't select from a list.
Add to the program so it first asks the user their choice as well as if they want to quit.
(It will be easier if you have them enter 1 for rock, 2 for paper, and 3 for scissors.)
Add conditional statements to figure out who wins and keep the records
When the user quits print a win/loss record

"""

import random

wins = 0
losses = 0
done = False
while not done:
    num = input("1 = rock  2 = paper  3 = scissors  4 = quit :")
    if num == "1":
        rock = random.randint(1, 3)
        if rock == 1:
            print("Rock, tie")
            print(wins, "-", losses)
            print()
        elif rock == 2:
            print("Paper, you lose")
            losses += 1
            print(wins, "-", losses)
            print()
        else:
            print("Scissors, you win")
            wins += 1
            print(wins, "-", losses)
            print()
    elif num == "2":
        paper = random.randint(1, 3)
        if paper == 2:
            print("Rock, you win")
            wins += 1
            print(wins, "-", losses)
            print()
        elif paper == 2:
            print("Paper, tie")
            print(wins, "-", losses)
            print()
        else:
            print("Scissors, you lose")
            losses += 1
            print(wins, "-", losses)
            print()
    elif num == "3":
        scissors = random.randint(1, 3)
        if scissors == 1:
            print("Rock, you lose")
            losses += 1
            print(wins, "-", losses)
            print()
        elif scissors == 2:
            print("Paper, you win")
            wins += 1
            print(wins, "-", losses)
            print()
        else:
            print("Scissors, tie")
            print(wins, "-", losses)
            print()
    elif num == "4":
        if wins > losses:
            print("You won", wins, "-", losses)
        elif wins < losses:
            print("You lost", wins, "-", losses)
        else:
            print("We tied", wins, "-", losses)
        done = True
    else:
        done = False
