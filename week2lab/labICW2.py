import csv #CSv to import data
total_records = 0 #cnts records
max = 0 #its max counts
min = 0 #its min counts
names = [] #list of names
max = [] #makes a max list
min = [] #makes a min list
over = [] #marks rooms that are over, hard a hard time figuring out how to make the process simple
omax = [] #marks rooms that are over, my best idea was to create two lists, one for max and one for min
omin = [] #I would then use those lists to run an index of the over names, nad hopfully that will count all the over rooms
ocnt = 0 #ocont counts the over rooms. i call this for the output
#my output is very bad. I feel i had to rig it to make it look good when there would have be an easier way. any recocmndeations would be appreciated

with open ("week2lab/lab2a.csv") as list: #imports the data in a loop
    olist = csv.reader(list) #reads the data in a loop
    print ("ROOM \t \t \t  MAX \t  MIN") #makes a terminal output. outside for loop so it doesn't print ever time
    for rec in olist:
        print(f"{rec[0]:17} \t {rec[1]:2} \t {rec[2]:2}") # prints the data in a loop
        names.append(rec[0]) #stores the names in a list
        max.append(int(rec[1])) #stores the max value in a list
        min.append(int(rec[2])) #stores the min value in a list
        total_records += 1 #count of total records
        if rec[2] > rec[1]: #reads the max over min. if that happens the data is transfered to a new list to call later
            over.append((rec[0])) #stores the over
            omax.append(int(rec[1])) #store the overmax
            omin.append(int(rec[2])) #stores the overmin
            ocnt += 1 #counts the over rooms,
print(f"processed {total_records} records") #total records displayed
print(f"there are {ocnt} records that are not fire legal") #displays the over
print("ROOM \t \t \t  MAX \t  MIN \t OVER") #header for output terminal
for index in range(0, len(over)): #for each over room the loop will read the over room and print it
    ilg = omax[index] - omin[index] #calculates the difference between the over max and over min, ilg is illegal. i can't spell
    print (f"{names[index]:17} \t  {omax[index]:2} \t  {omin[index]:2} \t {abs(ilg):0}") #dispplays the data, used abs to turn negative numbers into positive numbers