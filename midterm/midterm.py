# Brandon Medeiros
#Lab MidTerm individual
#2/5/24
#Libary------------------------
#display_menu(): #basic display menu
#allGames(): #has a header and index for statment to print all games in the list
#displayGames(attribute_list, attribute_name): #Uses two arguments, the first is for a list, the second is for what is being asked. attribute_name will be an enterd string while list will use the lists
#randomGame():#uses random.int to generate index number
#notice(attribute_list, atribute_name): #Gives user a list of options to chose from when picking a genre date etc.
#release_year_list = [] list of release year
# game_title_list = [] list of title
# genre_list = [] list of genre
# publisher_list = [] list of publisher
# platform_list = [] list of platform
# o = a true statment
# x = a false statment
import csv
import random #Random import. Uses a random number generator
#functions--
def display_menu(): #basic display menu
    print("\nMenu:")
    print("1. Display all games")
    print("2. Display games by genre")
    print("3. Display games by release year")
    print("4. Display games by platform")
    print("5. Give me a random game")
    print("6. Exit")
    return input("Enter your choice: ")
def allGames(): #has a header and index for statment to print all games in the list
    print(f"{'Release Year':13} {'title':36}\t{'Genre':20} {'publisher':23} {'Platform':8}")
    for index in range(0, len(release_year_list)):
        print(f"{release_year_list[index]:13} {game_title_list[index]:36}\t{genre_list[index]:20} {publisher_list[index]:23} {platform_list[index]:8}")
def displayGames(attribute_list, attribute_name): #Uses two arguments, the first is for a list, the second is for what is being asked. attribute_name will be an enterd string while list will use the lists
    attribute = input(f"\nEnter {attribute_name} to display games: ") #uses the inputed argument IE horror/action etc
    print(f"\nGames with {attribute_name} '{attribute}':")
    for i in range(len(game_title_list)): #list cycles the names
        if attribute_list[i] == attribute: #Finds a match to enterd attribute and prints all with that match
            print(f"{game_title_list[i]} ({release_year_list[i]}), Genre: {genre_list[i]}, Publisher: {publisher_list[i]}, Platform: {platform_list[i]}")
            #You found a hidden remark! Happy Grading!!!
def randomGame():
    index = randomnum() #useing random.int the index will become a random number, number is returned as an index.
    print(f"\nRandom Game: {game_title_list[index]} ({release_year_list[index]}), Genre: {genre_list[index]}, Publisher: {publisher_list[index]}, Platform: {platform_list[index]}")
def notice(attribute_list, atribute_name): #Gives user a list of options to chose from when picking a genre date etc.
    
   
    print(f"Here is a list of {atribute_name}'s Please chose from this list ")
    for index in range(0, len(release_year_list)):
        print(f"{attribute_list[index]}")
def randomnum(): #Forgot to add a return function. This function generates a ramdom number based on length of list, is called in the ran game function
    ran = random.randint(0, len(game_title_list) )
    return ran
#functions
release_year_list = []
game_title_list = []
genre_list = []
publisher_list = []
platform_list = []


with open("midterm/list2.csv") as csvfile:
    file = csv.reader(csvfile)
    for rec in file:
        
        release_year_list.append(rec[0])
        game_title_list.append(rec[1])
        genre_list.append(rec[2])
        publisher_list.append(rec[3])
        platform_list.append(rec[4])
#atr check Used to call diffrent lists I want to check for consistency
##for index in range(0, len(release_year_list)):
    #print(f"{genre_list[index]}")
#list check
#print(genre_list)

o = True
x = False

while o == True:
    menu_choice = display_menu()
    if menu_choice == "1":
        allGames()
    elif menu_choice == "2":
        notice(genre_list, "Genre")
        displayGames(genre_list, "Genre")
    elif menu_choice == "3":
        notice(release_year_list, "Release year")
        displayGames(release_year_list, "release_year_list")
    elif menu_choice == "4":
        notice(platform_list, "platform")
        displayGames(platform_list, "Platform")
    elif menu_choice == "5":
        randomGame()
    elif menu_choice == "6":
        o = x
    else:
        print("\n\tERROR\n")
print("Goodbye and happy Gaming")