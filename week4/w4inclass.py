#Brandon Medeiros
#w4 in class lab
#2/1/24

# Write a program that reads the data file (below) and stores the data into 1D parallel lists (remember, one list for every field).  Once the lists are populated (and the file is "closed"), process the lists to reprint the file data, record by record as they originally appear in the file.
#var dic
# fname = [] #first name "Greatest"
# lnanme = [] #last name "Ever"
# test1 = [] test1 score in list
# test2 = [] test2 score in list
# test3 = [] test3 score in list
#   avg = [] avg score in list test1+2+3/3
#     avg0 = 0 avg0 to start for loop
#     let_avg = [] letter avg a-f
#     total_count = 0 total count of students
#     class_avg = [] class average. avg of every student/number in list
#     cavg = 0 #0 cavg to start for loop
# all_students = [] #all data populated into a 2d list
import csv
fname = []
lnanme = []
test1 = []
test2 = []
test3 = []
with open ("week4/files/listPractice1-1.csv") as csvfile: #Hiiiiiiii. Same old meathod take the data format it to lists then work with lists
    file = csv.reader(csvfile)
    for rec in file:
        fname.append(rec[0])
        lnanme.append(rec[1])
        test1.append(int(rec[2])) #cast as int for math
        test2.append(int(rec[3]))
        test3.append(int(rec[4]))
print(f"{'FIRST':12}\t{'LAST':12}\t{'TEST1'}\t{'TEST2':}\t{'TEST3':}") #header

for index in range (0, len(fname)):
    print(f"{fname[index]:12}\t{lnanme[index]:12}\t{test1[index]}\t{test2[index]}\t{test3[index]}")
#basic index priting takes all data into lists and prints them to console
# Part 2

# Next, reprocess the lists to find each student's current average score along with the class average.  While processing in the for loop, store each student's average into a new list called 'avg' and reprint the records to include this numeric average.  Reprocess the lists one final time to find the letter equivalent of each student's average and store this into a new list called 'let_avg'.  Reprint the lists for a third time, record by record including average score and average letter equivalent.  After this third print of the original file data, print to the console the total number of student's in the class along with the class numeric average.      

    avg = [] #check var dic
    avg0 = 0
    let_avg = [] #or don't
    total_count = 0
    class_avg = [] #i do put work into it though
    cavg = 0
   
for i in range(0, len(test1)): #taking the data in range of 0-20 and using index and math to create an average t1-t3=total score/3 to get average
        avg0 = (test1[i] + test2[i] + test3[i]) / 3
        avg1 = float(f"{avg0:.2f}") #Making a new variable to convery the avg1 to a 2f float for a cleaner look
        avg.append(avg1)
        cavg = cavg + avg1 #Seeing as class average is just one variable decided to make a loop to count it up. could make a list but would have to append everything as "" just for one variable. That seemed like a looooot of work and i'm quite lazy
cavg = float(f"{cavg / len(fname):.2f}") #takes the total count of all students averages and divides it by the number of students


for i in range(0, len(fname)): #prints name and averag
        print(f"{fname[i]:12}\t{avg[i]:8}\t")
print(f"class average\t    {cavg}")
c_a = 0 
for i in range(0, len(fname)): #sorts the lists of student averages and assigns a grade then appends to let_avg
      if avg[i] >= 90:
            let_avg.append("A")
      elif avg[i] >= 80:
            let_avg.append("B")
      elif avg[i] >= 70:
            let_avg.append("C")
      elif avg[i] >= 60:
            let_avg.append("D")
      elif avg[i] < 60:
            let_avg.append("F")
        #one of my friends keeps talking about wanting to gnaw on my arm. I am worried. I keep getting distracted
      total_count += 1
for i in range(0, len(fname)): #simple print statment for all lists
        print(f"{fname[i]:12}\t{avg[i]:8}\t{let_avg[i]:8}")
print(f"class average:\t    {cavg}")
print(f"Total number of students in class: {total_count}")

# After your final display using the 1D parallel lists, create one new, empty list, that will become a 2D list.  Then, using a for loop and the 1D parallel lists, store the data to the 2D list you have created. Each index in the 2D list should contain a list of data. This list of data should contain the fname, lname, test1, test2, test3, num_average, and letter_average for the respective student.

# Process through this 2D list to display the data from the file (it should appear just like your previous 3 prints!)

all_students = [] #2d list

for i in range(0, len(fname)): #Appends all lists to the new 2d list
    #add each students data to their respective list
    all_students.append([fname[i], lnanme[i], test1[i], test2[i], test3[i], avg[i], let_avg[i]])
print(f"{'FIRST':10}\t{'LAST':10}\t{'TEST1':10}\t{'TEST2':8}\t{'TEST3':0}\t{'AVG&Let_AVG'}") #header
for i in range(0, len(all_students)): #Index of 2d list
    for x in range(0, len(all_students[i])): #X index of 2d list sorts the lists
        print(f"{all_students[i][x]:12} ", end="") #Final index print statment
    print()
print(f"Total number of students in class: {total_count}")
print(f"class average:\t    {cavg}")