import random
chambers = [0, 0, 0, 0, 0, 1]
def shuffle():
    random.shuffle(chambers)
    return chambers
#shuffle function-------------------
a = True
b = False
chambers = shuffle() #shuffles call both function
print(chambers) #
#shuffle function-------------------
def load(): #load function


    while a:
        chamberCheck()
        user_input = input(f"Enter the chamber number 1-{len(chambers)}: ")
        if user_input.isdigit():
            chamber_number = int(user_input) - 1
        elif user_input == "":
            chamber_number = chamberCheck() - 1
            if chamber_number >= 0 and chamber_number <= len(chambers) - 1:
                for i in range(len(chambers)):
                    if chambers[i] == 1:
                        chambers[i] = 0
                chambers[chamber_number] = 1
                a = b
            else:
                print("Invalid chamber number.")
        else:
            print("Invalid input. Please enter a number between 1 and 6.")
#load function-------------------
#menu function
def menu():
    #chamberCheck()
    print("1. Load Gun")
    print("2. Play Russian Roulette")
    print("3. Quit")
# load()
# print(chambers)
# chambers = shuffle()
# print(chambers)
def chamberCheck():
    for i in range(len(chambers)):
        if chambers[i] == 1:
            print(f"There are {len(chambers)} chambers remaining. Chamber {i + 1} is loaded.")
            return i+1
print(chamberCheck())

a = True
b = False
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
                print("Bang! You're dead!")
                for i in range(len(chambers)):
                    if chambers[i] == 1:
                        if chambers[i] == 1:
                            chambers[i] = "x"
                print(chambers)
            else:
                print("Click! You survived!")
                for i in range(len(chambers)):
                    if chambers[i] == 1:
                        if chambers[i] == 1:
                            chambers[i] = "x"
                            print(chambers)
            print(chambers)
            chambers.remove("x")
            print(chambers)
        if uInp2 == "n":
            if chambers[0] == 1:
                print("Bang! You're dead!")
                for i in range(len(chambers)):
                    if chambers[i] == 1:
                        if chambers[i] == 1:
                            chambers[i] = "x"
                print(chambers)
            else:
                print("Click! You survived!")
                for i in range(len(chambers)):
                    if chambers[i] == 1:
                        if chambers[i] == 1:
                            chambers[i] = "x"
                            print(chambers)
                print(chambers)
                chambers.remove("x")
                print(chambers)
    elif user_input == "3":
        a = b
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
