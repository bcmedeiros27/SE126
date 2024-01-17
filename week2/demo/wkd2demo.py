#W2D2 text file opening review +1d lists
import csv
total_records = 0
#create empty lists for each field
fnames = []
lnames = []
favenums = []
favanimals = []
with open("week2/demo/w2d2_demoTextFile.txt") as csvfile:
    #indent when connected to and reading file
    file = csv.reader(csvfile)
    for rec in file:
        print (rec)
        #append field data to the approite list(s)
        fnames.append(rec[0])
        lnames.append(rec[1])
        favenums.append(int(rec[2]))
        
        #len() --> returns length of structure (list) length of a list
        #the maximum length of rec is:

        if len(rec) == 4:
            

            favanimals.append(rec[3])
        else: #rec[3] does not exist
            favanimals.append("----")

#process fnames + favnimals list to display
for index in range(0, len(fnames)):
    print(f"{fnames[index]} fav animal is {favanimals[index]}")