#import lib
import csv
#get values
total_records = 0
total_salaries = 0
#int empty list 1-list per field
names = []
age = []
salary = []
#connect file
with open("week2/demo/example.csv") as unicorn:
    nahwhal = csv.reader(unicorn)
    #go in and "read each record in the file"
    for rec in nahwhal:
        #for every record found in the [file entire row of field data]
        print(f"{rec[0]:10} \t {rec[1]:3} \t {rec[2]:10}")
        #store data from rec list (current rec being read) to list
        #addign data to a list ---> .append() ; requires a list name as a starting object
        names.append(rec[0])#name
        age.append(int(rec[1]))#age
        salary.append(float(rec[2]))#salary
        #display the data in values in the NEAT colums
        #keep count of number of records
        total_records += 1
        #keep running total of salaries
        total_salaries += float(rec[2])
#final total display
print(f"TOTAL RECORDS: {total_records} | TOTAL SALARY: $ {total_salaries:.2f}")

#process the lists to display the text file information
#process list --> For loop

for index in range(0, total_records):
    #for each value in the range of 0 to # of times represented by total_records
    print(f"{index} {names[index]} is {age[index]} years old")

#process through the list to create a total age value
total_age = 0
for index in range(0, total_records):
    total_age += age[index]
    average_age = total_age / total_records
    print(f"Average age: {index}\t {average_age}")

total_age = 0
index = 0
while index < total_records:
    index +=1
    total_age += age[index]