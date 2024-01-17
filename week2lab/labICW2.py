import csv
total_records = 0
max = 0
min = 0
names = []
max = []
min = []
with open ("week2lab/lab2a.csv") as list:
    olist = csv.reader(list)
    print ("ROOM \t \t \t  MAX \t  MIN")
    for rec in olist:
        print(f"{rec[0]:17} \t {rec[1]:2} \t {rec[2]:2}")
        names.append(rec[0])
        max.append(int(rec[1]))
        min.append(int(rec[2]))
        total_records += 1
        
print(total_records)
for index in range(0, min):
    if min > max:
        print ("illegal")