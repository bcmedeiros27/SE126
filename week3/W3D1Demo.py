#w3d1 demo- text file handling and storing ID to lists
import csv

#total counter for all records
total_records = 0

print(f"{'desk':8} {'sds':8} {'processer':3} {'ram':3} {'hdd_1':5} {'num_hdd':3}{'hdd_2':5} {'os':4} {'year':4}")
with open ("week3/lab2b.csv") as csvfile:
    file = csv.reader(csvfile)
    for rec in file:
        #print(rec) #shows a list []
        #total_records += 1
        #print(total_records)


        #filtering for display----
        #--comp type-- rec[0]
        if rec[0] == "D":
                  comp_type = "desktop"
        elif rec[0] == "L":
                  comp_type = "laptop"
        else:
                  comp_type = "Error--" + str(rec[0])
        #manu Rec[1]
        if rec[1] == "DL":
                  manu = "dell"
        elif rec[1] == "GW":
                  manu = "Gateway"
        elif rec[1] == "HP":
                  manu = rec[1]
        else:
                  comp_type = "Error--" + str(rec[1])
        
         #processer ram hdd numhdd   

        processer = rec[2]
        ram = rec[3]
        hdd_1 = rec[4]
        num_hdd = rec[5]
        if rec[5] == "1":
                hdd_2 = "   "#"---"#none
                os = rec[6]
                year = rec[7]
        elif rec[5] == "2":
                hdd_2 = rec[6]
                os = rec[7]
                year = rec[8]
        else:
                hdd_2 = "Error --" + str(rec[5])
                os = "error"
                year = "errpr"

        #final print for each record
        print(f"{comp_type:8} {manu:8} {processer:3} {ram:3} {hdd_1:5} {num_hdd:3}{hdd_2:5} {os:4} {year:4}")
#Dc from file---------------------------------