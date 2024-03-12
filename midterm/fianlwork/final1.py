import random
import time
import sys
import os

typing_speed = 50 #wpm
def slow_type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)
    print ('')


chambers = [0, 0, 0, 0, 0, 1]
def shuffle():
    random.shuffle(chambers)
    return chambers
#shuffle function-------------------
a = True
b = False
c = True
d = False
o = True
x = False
chambers = shuffle() #shuffles call both function
print(chambers) #
#shuffle function-------------------




def load(): #load function
    global c
    global d
    c = o
    d = x
    #chamberCheck()
    while c:
        user_input = input(f"Enter the chamber number 1-{len(chambers)}: ")
        if user_input.isdigit():
            chamber_number = int(user_input) - 1
            if chamber_number >= 0 and chamber_number <= len(chambers) - 1:
                for i in range(len(chambers)):
                    if chambers[i] == 1:
                        chambers[i] = 0
                chambers[chamber_number] = 1
                c = d
            else:
                print("Invalid chamber number.")
        elif user_input == "":
            chamber_number = chamberCheck() - 1
            if chamber_number >= 0 and chamber_number <= len(chambers) - 1:
                for i in range(len(chambers)):
                    if chambers[i] == 1:
                        chambers[i] = 0
                chambers[chamber_number] = 1
                c = d
            else:
                print("Invalid chamber number.")
        else:
            print("Invalid input. Please enter a number between 1 and 6.")
#load function-------------------
#menu function
def menu():
    chamberCheck()
    print("1. Load Gun")
    print("2. Play Russian Roulette")
    print("3. 50/50 Load")
    print("4. Quit")
# load()
# print(chambers)
# chambers = shuffle()
# print(chambers)
def chamberCheck():
    for i in range(len(chambers)):
        if chambers[i] == 1:
            print(f"There are {len(chambers)} chambers remaining. Chamber {i + 1} is loaded.")
            return i+1
def bubblecham():
    sort_type = random.choice(['>', '<'])
    if sort_type == '>':
        for i in range(len(chambers)-1):
            for j in range(len(chambers)-1-i):
                if chambers[j] > chambers[j+1]:
                    chambers[j], chambers[j+1] = chambers[j+1], chambers[j]
    elif sort_type == '<':
        for i in range(len(chambers)-1):
            for j in range(len(chambers)-1-i):
                if chambers[j] < chambers[j+1]:
                    chambers[j], chambers[j+1] = chambers[j+1], chambers[j]

bubblecham()

while a:
    menu()
    user_input = input("Enter your choice: ")
    if user_input == "1":
        load()
        print(chambers)
    elif user_input == "2":
        uInp2 = input("Do you want to shuffle the chamber y/n:")
        if uInp2 == "y":
            chambers = shuffle()
            print(chambers)
            if chambers[0] == 1:
                slow_type("Bang! You're dead!")
                for i in range(len(chambers)):
                    if chambers[i] == 1:
                        if chambers[i] == 1:
                            chambers[0] = "x"
                            a = b
                print(chambers)
                slow_type(input("press enter to continue:"))
            else:
                slow_type("Click! You survived!")
                for i in range(len(chambers)):
                    if chambers[i] == 1:
                        if chambers[i] == 1:
                            chambers[0] = "x"
                            print(chambers)
            slow_type(input("press enter to continue:"))
            print(chambers)
            chambers.remove("x")
            chambers.append(0)
            print(chambers)
        if uInp2 == "n":
            if chambers[0] == 1:
                slow_type("Bang! You're dead!")
                for i in range(len(chambers)):
                    if chambers[i] == 1:
                        if chambers[i] == 1:
                            chambers[0] = "x"
                            a = b
                print(chambers)
            else:
                slow_type("Click! You survived!")
                for i in range(len(chambers)):
                    if chambers[i] == 1:
                        if chambers[i] == 1:
                            chambers[0] = "x"
                            print(chambers)
                slow_type(input("press enter to continue:"))
                print(chambers)
                chambers.remove("x")
                chambers.append(0)
                print(chambers)
            print(chambers)
    elif user_input == "3":
        bubblecham()
        print(chambers)
        
    elif user_input == "4":
        a = b
    else:
        print("Invalid choice. Please enter 1, 2, 3 or 4.")
print("end of game")