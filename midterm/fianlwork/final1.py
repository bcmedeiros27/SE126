#STARTING DOCUMENTATION WITH: name, program title, and PROGRAM PROMPT :D
#Brandon Medeiros
#Russian Roulette
#Create a list that can shuffle and move like an acutal chamber in a reolver that tracks and stays consistant in a while loop. Allow to user to minipulate the list (Reolver) and play russian rollute


import random # Important function that helps randomize chance or starting list
import time #used to add a cooltext function.
import sys #Used in the cooltext
import os

typing_speed = 50 
def slow_type(t): #slow text function. Using the function can change print statments to give dramatic flare
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)
    print ('')


chambers = [0, 0, 0, 0, 0, 1] #Main list, Chambers is the equivilent to a revolvers chamber. 6 chambers with an active round in one.
def shuffle(): #The shuffle function then shuffles the chambers to have the active round be random at the start.
    random.shuffle(chambers)
    return chambers
#shuffle function-------------------
a = True #True false statments to be used to break while loops. Plz let me use breaks T_T, I want to be laaaazy.
b = False
c = True
d = False
o = True
x = False
chambers = shuffle() 
print(chambers) #Print statments with chambers are sprinkled throughout to program to keep track of the list. From a user perspective it makes the game less random and these all can be commented out but for the sack of demoing the program it shows how things run and gives you an idea of inner workings.
#shuffle function-------------------




def load(): #load function
    global c
    global d
    c = o
    d = x
    #chamberCheck()--commented out for tresting purposes
    while c:
        user_input = input(f"Enter the chamber number 1-{len(chambers)}: ")
        if user_input.isdigit(): #trap to keep user from inputing random numbers or letters to break input
            chamber_number = int(user_input) - 1
            if chamber_number >= 0 and chamber_number <= len(chambers) - 1:
                for i in range(len(chambers)):
                    if chambers[i] == 1:
                        chambers[i] = 0
                chambers[chamber_number] = 1
                c = d
            else:
                print("Invalid chamber number.")
        elif user_input == "": #Since a bullet is alreayd stored allows to user to give no input, will then call the stored value instead of input value
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
    #its a menu! It has print statments! Neat!
# load()--Comented out old code for testing
# print(chambers)--
# chambers = shuffle()--
# print(chambers)--commented out of code for test
def chamberCheck(): 
    for i in range(len(chambers)):
        if chambers[i] == 1:
            print(f"There are {len(chambers)} chambers remaining. Chamber {i + 1} is loaded.") #useing len of the chambers list and chamber index to dynamicly update
            return i+1
def bubblecham(): #Using bubble sort to create a random situation
    sort_type = random.choice(['>', '<']) #since the higest value is 1 it will either be placed first or last. using random we can make it intresting by making the first chamber active or not.
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

#--gimme some internal documentation in here :D
#bubblecham()

while a: #Main while loop. Calls most defs here to create the game
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
                    if chambers[i] == 1: #If statment to check chamber at index 0 = 1. if so round is active and game ends
                        if chambers[i] == 1:
                            chambers[0] = "x"
                            useInp3 = input("Play again y/n:")
                            if useInp3 == "y":
                                a = a
                            else:
                                a = b
                chambers.remove("x")
                chambers.append(0)
                print(chambers)
                slow_type(input("press enter to continue:"))
            else:
                slow_type("Click! You survived!")
                for i in range(len(chambers)):
                    if chambers[i] == 1:
                        if chambers[i] == 1:
                            chambers[0] = "x" #appends [0] as x for easy removeable.
                            print(chambers)
            slow_type(input("press enter to continue:"))
            print(chambers)
            chambers.remove("x") #removes x from the list
            chambers.append(0) #appends another 0 to the list so it becomes 6
            chambers[0] = 1 #Since the active round is now gone a new one is made
            chambers = shuffle() #shuffles the new rounds
            print(chambers)
        if uInp2 == "n":
            if chambers[0] == 1:
                slow_type("Bang! You're dead!")
                for i in range(len(chambers)):
                    if chambers[i] == 1:
                        if chambers[i] == 1:
                            chambers[0] = "x"
                            useInp3 = input("Play again y/n:")
                            if useInp3 == "y":
                                a = a
                            else:
                                a = b
                chambers.remove("x")
                chambers.append(0)
                chambers[0] = 1
                chambers = shuffle()
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
