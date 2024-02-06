import csv
#create 1d lists [Parallel to each other]
#base lists on fields in the file

fname = []
lnanme = []
test1 = []
test2 = []
test3 = []

#connect to the file and read data

with open ("week4/files/listPractice1-1.csv") as csvfile:
    file = csv.reader(csvfile)
    #come back and show print(file later)
    for rec in file:
        #store data from file fields to respective list
        #Parallel - sotrin inital file record data at same position (index)
        fname.append(rec[0])
        lnanme.append(rec[1])
        test1.append(int(rec[2])) #cast as int for math
        test2.append(int(rec[3]))
        test3.append(int(rec[4]))
#disconnected from file -----------------

#process the lists -----> for loop
print(f"{'FIRST':12}\t{'LAST':12}\t{'TEST1':}\t{'TEST2':}\t{'TEST3':}")
print("--------------------------------------------------------------")
for index in range (0, len(fname)):
    #len returns length of item for items in list
    print(f"{fname[index]:12}\t{lnanme[index]:12}\t{test1[index]}\t{test2[index]}\t{test3[index]}")
print("--------------------------------------------------------------")
#calculate and store each students average test sore
avg = 0
total_count = 0
average = []
for i in range(0, len(test1)):
    #caculate avg of student
    avg = (test1[i] + test2[i] + test3[i]) / 3
    avg1 = float(f"{avg:.2f}")
    average.append(avg1)
#displays studens fname and average
print(f"{'first':12}\t{'Average':12}")
for i in range(0, len(fname)):
    print(f"{fname[i]:12}{average[i]:8}")
#display total student in file higest test average and score
#sequential search search in sequance though and end
low_name = ""
low_avg = 100 #starts with higest value to drop and find the lowest
hi_name = ""
hi_avg = 0
for i in range(0, len(average)):
    #determine if current average is lower then then current low_avg
    if average[i] < low_avg:
        low_avg = average[i]
        low_name = fname[i]
    if average[i] > hi_avg:
        hi_avg = average[i]
        hi_name = fname[i]
#display
print(f"Students in file: {len(fname)}")
print(f"Lowest average: {low_name} - {low_avg:.1f}")
print(f"Lowest average: {hi_name} - {hi_avg:.1f}")
#2d----Lists----------------------------------------
#use your 1d parallel list to populate a new, 2d list
#2d list is a list with with lists :>
all_students = []

for i in range(0, len(fname)):
    #add each students data to their respective list
    all_students.append([fname[i], lnanme[i], test1[i], test2[i], test3[i], average[i]])
#display the 2d lists to the console, for now just get the lists to display ie [Floyd,Eastham,100,85,93]
for i in range(0, len(all_students)):
    print(f"{all_students[i]}")
#display 2d list to the conole where each value or list appears as a value and not a list item
for i in range(0, len(all_students)):
    #we have lists withen a list - otter for handles main list(all students)
        #inner handles each value found at current list (all students i)
        for x in range(0, len(all_students[i])):
            print(f"{all_students[i][x]} ", end="")
            #include an extra emprty print() to cancle the interior prints's end = ""
        print()
#A 90+
#B 80-89
#C 70-79
#D 60-69
#F <60

#if average[i] >= 90
    #let_avg.append("a")
#elif average[i] > = 80:   
    #let_avg.append("b")