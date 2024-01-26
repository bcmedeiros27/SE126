# Construct a program that will analyze potential voters. The program should generate the following totals:

#     Number of individuals not eligible to register.
#     Number of individuals who are old enough to vote but have not registered.
#     Number of individuals who are eligible to vote but did not vote.
#     Number of individuals who did vote.
#     Number of records processed.
#brandon Medeiros
#Week #3 - lab homework
#1/26/2024
# total_records = 0
# ss = []
# ssct = 0
# age = [] #age
# reg = [] #reg
# vote = [] #voe
# unelg = 0
# unabreg = [] #new list
# oldneg = [] #old
# regnvote = [] #new list
# regdvite = [] #new list for votes




import csv
total_records = 0 #total records
ss = [] #ss list
ssct = 0 #counter for tests
age = [] #age
reg = [] #reg
vote = [] #voe
unelg = 0 #co
unabreg = [] #new list
oldneg = [] #old
regnvote = [] #new list
regdvite = [] #new list for votes
# unabregc = 0 counter for unable to register
# oldnegc = 0 counter for old enough to vote but have not registered
# regnvotec = 0 counter for eligible to vote but did not vote
# regdvite = 0  counter for vote
# test = 0  just a test. HIIIIIII!
with open ("week3/week3idv/voters_202040.csv") as csvfile:
    file = csv.reader(csvfile)
    for rec in file: #opens files, appends lists to be used
        ssct += 1
        total_records += 1
        ss.append(int(rec[0])) #appends to ss list
        age.append(int(rec[1])) #appends to age list
        reg.append(rec[2]) #appends to reg list
        vote.append(rec[3]) #appends to vote list
for index in range(0, (ssct)): #Using SS as a base index to go through data and make appends
    if age[index] <= 17: #appens those who can't vote to be called later
        unabreg.append(reg[index])
        #regnvote.append("")
    if age[index] >= 18: #appens those who can  vote to be called later
            unabreg.append("")
    if age[index] >= 18 or age[index] <= 17: #Checks age and register to be called later
         if reg[index] == "Y":
             oldneg.append(vote[index])
         else:
             
             oldneg.append("") #appends list for empty fields to be blank
    if age[index] >= 18 or age[index] <= 17 and reg[index] == "Y" and vote[index] == "Y": #Checks age, reg index, and voter index to create a new list
        regnvote.append(reg[index])
    else:
         regnvote.append("") #appens blank if specifations not met
       
   
    if reg[index] == "Y" and vote[index] == "Y": #Voter checker just checks y and Y
         regdvite.append(vote[index])
    else:
         regdvite.append("") #appens blank if specifations not met
         
# print(f"{unabreg}")       
# print(f"{oldneg}")
# print(f"{regnvote}")

# print(f"{regdvite}")
# print(f"{total_records}") #Test outputs to check terminal
unabregc = 0
oldnegc = 0
regnvotec = 0
regdvite = 0 
test = 0 
for index in range(0, (total_records)): #Using total records as a base index to go through data and make appends
     if unabreg[index] == "N": #Voter checker just checks then adds to verable list
           unabregc += 1
     if oldneg[index] == "N": #same as before, create the lists first, call them in the for loop, and add to count
          oldnegc += 1
     if regnvote[index] == "N": #same as before, create the lists first, call them in the for loop, and add to count
          regnvotec += 1
     if vote[index] == "Y": #same as before, create the lists first, call them in the for loop, and add to count
          regdvite += 1
print(f" {'ss':4} {'age':3} {'reg':3} {'vote':3}") #header for data output
for index in range(0, (total_records)):
     print(f"{ss[index]:5} {age[index]:3} {reg[index]:3} {vote[index]:3}") #data index put in a and put in a readable output
print(f"there are {unabregc} people unable to registar" )
print(f"there are {oldnegc} people old enough to registar but did not") 
print(f"there are {regnvotec} people eligable to vote but did not" )
print(f"there are {regdvite} who are eligable and did vote" )
print(f"there where {total_records} processed") 

# print(f"{unabregc}")
# print(f"{oldnegc}")       
# print(f"{regnvotec}")
# print(f"{regdvite}") More terminal data

print("Goodbye! Goodbye")         

        