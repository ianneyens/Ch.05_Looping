'''
ROSHAMBO PROGRAM
----------------

Create a program that randomly prints 1, 2, or 3.
Expand the program so it randomly prints rock, paper, or scissors using if statements. Don't select from a list.
Add to the program so it first asks the user their choice as well as if they want to quit.
(It will be easier if you have them enter 1 for rock, 2 for paper, and 3 for scissors.)
Add conditional statements to figure out who wins and keep the records
When the user quits print a win/loss record

'''

import random

wins = 0
losses = 0
done = False
while not done:
    num = random.randint(1, 3)
    x = float(input("1 = rock  2 = paper  3 = scissors  4 = quit :"))
    if num == 1:
        print("rock")
        if x == 1:
            print("Tie game")
            print(wins, "-", losses)
        elif x == 2:
            print("You win")
            wins += 1
            print(wins, "-", losses)
        elif x == 3:
            print("You lose")
            losses += 1
            print(wins, "-", losses)
        else:
            done = True
            print(wins, "-", losses)
    elif num == 2:
        print("paper")
        if x == 1:
            print("You win")
            wins += 1
            print(wins, "-", losses)
        elif x == 2:
            print("Tie game")
            print(wins, "-", losses)
        elif x == 3:
            print("You lose")
            losses += 1
            print(wins, "-", losses)
        else:
            done = True
            print(wins, "-", losses)
    elif num == 3:
        print("scissors")
        if x == 1:
            print("You lose")
            losses += 1
            print(wins, "-", losses)
        elif x == 2:
            print("You win")
            wins += 1
            print(wins, "-", losses)
        elif x == 3:
            print("Tie game")
            print(wins, "-", losses)
        else:
            done = True
            print(wins, "-", losses)
