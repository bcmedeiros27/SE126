#Brandon Medeiros Lab #1, Date 1/9/24
#program Prompt and any necessary starting notes
#You will be writing one Python file for this project - it is a program that determines whether a meeting room is in violation of fire regulations regarding the maximum room capacity. The program will accept the maximum room capacity and the number of people attending the meeting. If the number of people is less than or equal to the maximum room capacity, the program announces that it is legal to hold the meeting and tells how many additional people may legally attend. If the number of people exceeds the maximum room capacity, the program announces that the meeting cannot be held as planned due to the fire regulation and tells how many people must be excluded in order to meet the fire regulations. The user should be allowed to enter and check as many rooms as they would like without exiting the program.
#Internal documentation
#old way: Arguments place = 0 Call(place) and can be filled. New way: can call function without variable by adding function to input call(input) makes things cleaner.



def difference(people, max_cap): #function to calculate difference
    if people > max_cap: #if people is greater than max_cap, returns neg # this will be used later
        unsafe = max_cap - people
        #print(f"You most remove {unsafe} people from the meeting to meet fire regulations")
        #print(f"{name} meeting is not fire legal")
        return int(unsafe) #returns negative number
    elif people < max_cap:
        safe = max_cap - people #if people is less than max_cap, returns pos # used later
        #print(f"{safe} people can be added to the meeting and still meet fire regulations")
        #print(f"{name} meeting is fire legal")
        return int(safe) #returns safe to be used later


def decision(response): #detects response to trap question. y or n.lower
    while response != "y" and response != "n": #only two options covers both forces trap question to be y or n
        response = input("Please enter a valid response y/n:").lower()
        
    return response # returns response to be used later
def checker(number):#same logic as decision but for numbers
  while not number.isdigit():#can only add numbers
    number = input("Please enter people as a valid number: ")
  return int(number)#returns number as a number

loop = "y" # basic loop to keep program running
while loop == "y":
    name = input("Name of meeting: ") #user input for name of meeting
    people = checker(input("number of people attending:")) #user input for number of people attending
    max_capacity = checker(input("maximum room size:"))#user input for max capacity
    command = difference(people, max_capacity)#creates command variable to be used late
    if command is not None:  # Check for None before performing the comparison
        if command >= 1:  # Nested if statement to handle the None case, if command >1 the meeting is safe
          print(f"the {name} is fire legal. you can add {command} more people to {name} to meet max fire regulations")
          trap = decision(input("Would you like to check another room? (y/n)"))#trap question to check if user wants to check another room
          loop = trap#continues loop
        else:#if command is less than 1 or a negitive number as set up eariler, the meeting is unsafe
          print(f"The {name} meeting is not fire legal! and {abs(command)} most be removed to be fire legal")#abs(command) is used to make the number positive)
          trap = decision(input("Would you like to check another room? (y/n)"))#trap question to check if user wants to check another room
          loop = trap#continues loop
    else: #if 0 none can be added or removed. the room is safe.
      print(f"{name} is fire legal. No one can be added or needs to be removed you are at max capacity for {name}.")
      trap = decision(input("Would you like to check another room? (y/n)"))#trap question to check if user wants to check another room
      loop = trap#continues loop
print("Goodbye")