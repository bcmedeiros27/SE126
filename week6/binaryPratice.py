import csv

type_ = []
name = []
meaning = []
origin = []

with open("week6/party.csv", encoding="utf-8") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        type_.append(rec[0])
        name.append(rec[1])     #What we sort and search
        meaning.append(rec[2])
        origin.append(rec[3])
#sort the file data by firs tname, ascending order (increasing)
#Create a loop for user to search repeatadly
#pre form binary search
#Binary search--------------------------------------------------
#orginal file print
print("Orginal-----------------------------------------")
print(f"{'type':8} {'name':12} {'meaning':30} {'origin'}")
for i in range(0, len(type_)):
    print(f'{type_[i]:8}{name[i]:12}{meaning[i]:30}{origin[i]}')

#BUBBLE SORT----------------------------------------

for i in range(0, len(name) - 1):#outter loop

    


    for index in range(0, len(name) - 1):#inner loop

       
        #below if statement determines the sort

        #list used is the list being sorted

        # > is for increasing order, < for decreasing

        if(name[index] > name[index + 1]):

            

            #if above is true, swap places!

            temp = name[index]

            name[index] = name[index + 1]

            name[index + 1] = temp

 
            #swap all other values
            #--type--
            temp = type_[index]

            type_[index] = type_[index + 1]

            type_[index + 1] = temp
            #--meaning--
            temp = meaning[index]

            meaning[index] = meaning[index + 1]

            meaning[index + 1] = temp
            #--origin--

            temp = origin[index]

            origin[index] = origin[index + 1]

            origin[index + 1] = temp
#Test data to see that is has ordered
print("Sorted---------------------------------------------")
print(f"{'type':8} {'name':12} {'meaning':30} {'origin'}")
for i in range(0, len(type_)):
    print(f'{type_[i]:8}{name[i]:12}{meaning[i]:30}{origin[i]}')
answer = "y"
while answer.lower() == "y":
    search = input("Enter a name to search")

    #The algorithm for binary search



    #Binary Search Algorithm:



    min = 0

    max = len(name) - 1       #can also use len(listName) for 'records' value


    mid = int((min + max) / 2)

    #this is for INCREASING order

    while (min < max and search.lower() != name[mid].lower()):

        if search < name[mid]:

            max = mid - 1

        else:

            min = mid + 1

        mid = int((min + max) / 2)

    if search.lower() == name[mid].lower():
        print(f"Found {search}")
        print(f"{type_[mid]:8}{name[mid]:12}{meaning[mid]:30}{origin[mid]}")
        #found them! use 'mid' for index of found search item

    else:
        print(f"Did not find {search} try again")

        #boooo not found

    answer = input("\tWould you like to search again? [y/n]:")