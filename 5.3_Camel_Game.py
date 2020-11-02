'''
CAMEL GAME
----------
The pseudo-code for how to code this game is in Chapter 5 of the Python Jedi book
'''

import random
done = False

canteen = 3
camel = 0
thirst = 0
miles_traveled = 0
natives = -20

print()
print("Welcome to the Camel Game")
print("The idea is to ride your camel 200 miles across the desert while being chased.")
print("You need to manage your thirst, how tired your camel is, and how far ahead of the natives you are.")
print("Good Luck and have fun")
print()

while not done:

    print("1. Drink from canteen")
    print("2. Ahead moderate speed")
    print("3. Ahead full speed")
    print("4. Stop for the night")
    print("5. Status check")
    print("6. Quit")
    print()

    user_input = input("What would you like to do :")

    if user_input == "1":                                        # drink from canteen
        canteen -= 1
        thirst = 0
        print("You have", canteen, "drinks remaining")
        print("You have traveled", miles_traveled, "miles")
        print()
    elif user_input == "2":
        miles = random.randint(5, 12)                            # ahead moderate speed
        natives_traveled = random.randint(7, 12)
        camel += 1
        thirst += 1
        miles_traveled += miles
        natives += natives_traveled
        print("You have travelled", miles_traveled, "miles")
        print()
    elif user_input == "3":                                     # ahead full speed
        miles = random.randint(10, 20)
        thirst += 1
        camel_tired = random.randint(1, 3)
        camel += camel_tired
        miles_traveled += miles
        natives_traveled = random.randint(12, 17)
        natives += natives_traveled
        print("You have travelled", miles_traveled, "miles")
        print()
    elif user_input == "4":                                     # Stop for the night
        camel = 0
        natives_traveled = random.randint(7, 15)
        natives += natives_traveled
        print("Your camel thanks you")
    elif user_input == "5":                                     # Status check
        print(miles_traveled)
        print(canteen)
    elif user_input == "6":                                     # Quit
        print("Quitter")
        break
    else:
        done = False

    if miles_traveled >= 200:
        print("Congratulations, you won!")
        break
    else:
        done = False
    if natives >= miles_traveled:
        print("The natives have caught you and eaten you for dinner")
        print("You traveled", miles_traveled, "miles")
        break
    else:
        done = False
    if thirst >= 4:
        print("You are thirsty")
    elif thirst >= 6:
        print("You have died of thirst")
        print("You traveled", miles_traveled, "miles")
        break
    else:
        done = False
    if camel >= 5:
        print("Your camel is getting tired and needs to rest")
    elif camel >= 8:
        print("You killed your camel and the natives have caught up to you")
        print("You traveled", miles_traveled, "miles")
        break
    else:
        done = False
