#wd7 comparing search moethods
#This demo covers: Sequaential search (review), binary searcdh (intro), bubble sory (intro)
#--Lib---
import csv
#--Funct--

#--main code--
#Create empty 1d list
id_stud = []
lname = []
fname = []
class1 = []
class2 = []
class3 = []

with open ("week6/w7_demoFile.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:

        id_stud.append(rec[0])
        lname.append(rec[1])
        fname.append(rec[2])
        class1.append(rec[3])
        class2.append(rec[4])
        class3.append(rec[5])
#check file
for i in range(0, len(id_stud)):
    print(f"{id_stud[i]} {lname[i]} {fname[i]}")
#Seq search ask user for search name
#found = -1
found = [] #Allows for duplicates in list
search_name = input("Please enter name:")
seq_count = 0
# for i in range(0, len(lname)):
#     if search_name.lower() == lname[i].lower(): #.lower
#         #Store found values location(index)
#         found = i
for i in range(0, len(fname)):
    if search_name.lower() == fname[i].lower(): #.lower
        #Store found values location(index)
        found.append(i)
        seq_count += 1
if found[0] != "":
    print(f"found {search_name} at index postion: {found}")
    print("\tHere is the info")
    for i in range(0, len(found)):
        print(f"\t\t {fname[found[i]]} {lname[found[i]]} {id_stud[found[i]]} {class1[found[i]]} {class2[found[i]]} {class3[found[i]]}")
else:
    print("Could not ifne name")
print(f"Search complete. search loop ran {seq_count} iterations")

#binary search -- take an ordered list and divide it into 2 seacons (high, low) and based on a MIDDLE POINT will continually halve the search pool until a unique value is found (or one isn't)

search_name = input("Please enter LastNAME:")

min = lname[0] #first postion of the life
max = lname[len(lname) -1 ]#Take length and subtract 1
#mid = int((0 + len(lname) -1) / 2)
mid = int((min + max)/ 2)
bin_count = 0

while (min < max and search_name != lname[mid]):
    bin_count += 1
    if search_name < lname[mid]:
        max = mid -1
    else:
        min = mid +1
    mid = int((min + max ) / 2)

if search_name == lname[mid]:
    for i in range(0, len(found)):
        print(f"\t\t {fname[mid]} {lname[mid]} {id_stud[mid]} {class1[mid]} {class2[mid]} {class3[mid]}")
else:
    print("Could not ifne name")