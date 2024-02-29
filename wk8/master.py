import csv

#Var =================================================================
iD = [] #Basic lists of CSV data
last = []
first = []
ca1 = []
ca2 = []
ca3 = []
O = True #true flase statments for menu
X = False

#DEF =================================================================
def menu (): #Menu its a menu
    print("Menu:")
    print("1. See All Student Report")
    print("2. Search for a Student [ID]")
    print("3. Search for a Student [Last]")
    print("4. View a Class Roster [class1, class2, and class3]")
    print("5. Exit/Quit Program")
    choice = input("Enter your choice: ")
    return choice
def classS(class_name): #Sequential class search
    found_class = [] #creates 2d of ID's First and Last
    for i in range(len(iD)): #Checks the Class name input compared to the CA list's and if matchs appends ID First and Last
        if class_name.lower() in ca1[i].lower() or class_name.lower() in ca2[i].lower() or class_name.lower() in ca3[i].lower():
            found_class.append((iD[i], last[i], first[i], ca1[i], ca2[i], ca3[i]))
    
    if found_class: #Takes the 2d list and prints it out
        print(f"Students in {class_name} class:")
        for student in found_class:
            print(f"ID: {student[0]} Last: {student[1]:10} First: {student[2]}")
            
           
    else:
        print(f"No students found in {class_name} class.")
def binSearch(name): #Binary search. This is bassicly magic to me? I understand the concept but not the execution 
    min = 0
    max = len(last) - 1

    while min <= max:
        mid = (min + max) // 2
        if last[mid].lower() == name.lower(): #Uses index number of the last list along with math to determine the index....i think?
            return mid
        elif last[mid].lower() < name.lower():
            min = mid + 1
        else:
            max = mid - 1

    return -1
def binSearchID(iD1): #Another binary search, Who even came up with this idea. Its crazy.
    min = 0
    max = len(iD) - 1

    while min <= max:
        mid = (min + max) // 2
        if iD[mid].lower() == iD1.lower(): #Takes the ID index along with max to determine the index....i think?
            return mid
        elif iD[mid].lower() < iD1.lower():
            min = mid + 1
        else:
            max = mid - 1

    return -1
#CSVREADER==================================================================
with open("wk8/lab5_students.csv") as csvfile: #Basic csv reader
    file = csv.reader(csvfile)
    for rec in file:
        iD.append(rec[0])
        last.append(rec[1])
        first.append(rec[2])
        ca1.append(rec[3])
        ca2.append(rec[4])
        ca3.append(rec[5])
# for i in range(0, len(iD)) : """Print statments to check how the program was running"
#     print (iD[i], last[i], first[i], ca1[i], ca2[i], ca3[i])
#Menu Console
loop = O #Loop for the menu
while loop == O:
    choice = menu()
    
    if choice == "1":
        # See All Student Report
        for i in range(len(iD)):
            print(f"{iD[i]} {last[i]:10} {first[i]:8} {ca1[i]} {ca2[i]} {ca3[i]}")
    
    elif choice == "2":
        # Search for a Student [ID]
        iD1 = input("Enter the ID of the student: ")
        index1 = binSearchID(iD1)
        if index1 != -1:
            print("Student found:")
            print("ID:", iD[index1])
            print("First Name:", first[index1])
            print("Last Name:", last[index1])
        else:
            print("Student not found.")
    
    elif choice == "3":
        # Search for a Student [Last]
        name = input("Enter the last name of the student: ")
        index = binSearch(name)
        if index != -1:
            print("Student found:")
            print("ID:", iD[index])
            print("First Name:", first[index])
            print("Last Name:", last[index])
        else:
            print("Student not found.")
    
    elif choice == "4":
        # View a Class Roster [class1, class2, and class3]
        class_name = input("Enter the class name: ")
        classS(class_name)
    
    elif choice == "5":
        # Exit/Quit Program
        loop = X 
        
    
    else:
        print("Invalid choice. Please try again.")
print("Goodbye")