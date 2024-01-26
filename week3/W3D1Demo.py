#w3d1 demo- text file handling and storing ID to lists
import csv

#total counter for all records
total_records = 0
#create lists
comp_type_list = []
manu_list = []
processer_list = []
ram_list = []
hdd_1_list = []
num_hdd_list = []
hdd_2_list = []
os_list = []
year_list = []
print(f"{'desk':8} {'Manu':9} {'processer':10} {'ram':3} {'hdd_1 |':5} {'num_hdd|':7} {'hdd_2 |':5} {'os':4} {'year':5}")
with open ("week3/lab2b.csv") as csvfile:
    file = csv.reader(csvfile)
    for rec in file:
        #print(rec) #shows a list []
        total_records += 1
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
        #append respective values to the approproiate field list
        comp_type_list.append(comp_type)
        manu_list.append(manu)
        processer_list.append(processer)
        ram_list.append(ram)
        hdd_1_list.append(hdd_1)
        num_hdd_list.append(num_hdd)
        hdd_2_list.append(hdd_2)
        os_list.append(os)
        year_list.append(year)
        #final print for each record
        #print(f"{comp_type:8} {manu:8} {processer:3} {ram:3} {hdd_1:5} {num_hdd:3}{hdd_2:5} {os:4} {year:4}")
#Dc from file---------------------------------

#process the list to print the machine data
print (total_records)
for index in range(0, (total_records)):
        print(f"{comp_type_list[index]:8} {manu_list[index]:9} {processer_list[index]:10} {ram_list[index]:3} {hdd_1_list[index]:5}\t\t{num_hdd_list[index]:4}{hdd_2_list[index]:5}  {os_list[index]:4} {year_list[index]:5}")
        
        #the length of one of our lists ->len function when passed a list retruns the interger count of values
#process the lists to: count the number of desktops
desktop_count = 0
laptop_count =0 
for index in range(0, len(comp_type_list)):
        if comp_type_list[index] == "desktop" and int(year_list[index]) <= 16:
                desktop_count += 1
        if comp_type_list[index] == "laptop" and int(year_list[index]) <= 16:
                laptop_count += 1
# print(f"{desktop_count}")
# print(f"{laptop_count}")               
        #look through comptypelist to find deskto
print(f"if will cost ${desktop_count*2000} to replace {desktop_count} desktops with OS 2016 and older")
print(f"if will cost ${laptop_count*1500} to replace {laptop_count} laptops with OS 2016 and older")
# for index in range(0, len(hdd_1_list)):
#         if hdd_1_list[index] == "001TB":
#                 total_size += 1
#         else:
#                 total_size += 0.5
#         count_size += 1
#average = total_size / count_size # could use len hdd1 list or total records in place of count size
#print(f"Average HDD#1 size {average:0.2f}TB or {average*1000:0.2f}GB")