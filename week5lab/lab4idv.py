# In Python, process the text file “lab4A_GOT_NEW.txt” to store each field into its own corresponding list:

# This means you will have 1D parallel lists for this file! 
# Firstname0            Lastname1            Age 2                       Nickname3            House Allegiance4
# Brandon Medeiros
#Lab#4 individual
#2/5/24
#Var dic
# WOW Huge list...
# fname = [] #First name
# lnanme = [] #last name
# age = [] #age
# nick = [] #nickname
# h_a = [] #house alliance
# ttl = 0 #ttl members
# avga = 0 #avverage age added up
# tavga = 0 #average age divded by total people
# hs = 0 #house stark
# hslf = [] house stark first name
# hsll = [] House Stark last name
#This is going to be the same for like the rest of the lines
# hb = 0  #house Baratheon
# hbf = [] #house Baratheon first name
# hbl = [] #house Baratheon Last name
# ht = 0 #House tully
# htf = [] #House tully first name
# htl = [] #house Tully Last name
# nw = 0 #Nights Watch
# nwf = [] #Nights watch first name
# nwl = [] #Nights watch last name
# hl = 0 #House Lannister
#Hey! #Did you read all the books?
# hlf = [] House lannister first name
# hll = [] #House Lannister last name
# hta = 0 #house targaryen
#Is it a bad that Viserys and Jaime are some of my favorites?
# htaf = [] House Targaryen first name
# htal = [] house targaryen last name
import csv #Same song and dance import, list, compile
fname = []
lnanme = []
age = []
nick = []
h_a = []
with open ("week5lab/files/lab4A_GOT_NEW.csv") as csvfile: #Compiles list
    file = csv.reader(csvfile)
    for rec in file:
        fname.append(rec[0])
        lnanme.append(rec[1])
        age.append(int(rec[2]))
        nick.append(rec[3])
        h_a.append(rec[4])
print(f"{'Firstname':9}\t{'Lastname':9}\t{'Age':1}\t{'Nickname':18}\t{'House Allegiance':15}") #Header for first print
h_m = [] #House mottos to later be added and appened to new list
for index in range (0, len(fname)):
    print(f"{fname[index]:9}\t{lnanme[index]:9}\t{age[index]}\t{nick[index]:18}\t{h_a[index]:15}") #Print list for basic data
for index in range (0, len(fname)): #Using if elif == to sort through h_a list and append appropriate motos to h_m list
    if h_a[index] == "House Stark":
        h_m.append("Winter is Coming")
    elif h_a[index] == "House Baratheon":
        h_m.append("Ours is the fury.")
    elif h_a[index] == "House Tully":
        h_m.append("Family. Duty. Honor.")
    elif h_a[index] == "Night's Watch":
        h_m.append("And now my watch begins.")
    elif h_a[index] == "House Lannister":
        h_m.append("Hear me roar!") # Ai auto completed this as "h_m.append("I am the Lannister.")" the fact hear my roar is the real motto is funny.
    elif h_a[index] == "House Targaryen":
        h_m.append("Fire & Blood")
print(f"{'Firstname':9}\t{'Lastname':9}\t{'Age':1}\t{'Nickname':18}\t{'House Allegiance':15}\t{'House Mottos'}") #New header with motto
for index in range (0, len(fname)): #Compileslist with added h_m
    print(f"{fname[index]:9}\t{lnanme[index]:9}\t{age[index]}\t{nick[index]:18}\t{h_a[index]:15}\t\t{h_m[index]:15}")
#Check Var dic
ttl = 0 
avga = 0
tavga = 0
hs = 0
hslf = []
hsll = []
hb = 0
hbf = []
hbl = []
ht = 0
htf = []
htl = []
nw = 0
nwf = []
nwl = []
hl = 0
hlf = []
hll = []
hta = 0
htaf = []
htal = []
for index in range (0, len(h_a)): #Appends first name and last name to a list to be called in a for loop for tally of each house. Was going to try a 2d list but couldn't get it to print well
    if h_a[index] == "House Stark":
        hs += 1
        hslf.append(fname[index])
        hsll.append(lnanme[index])
    elif h_a[index] == "House Baratheon":
        hb += 1
        hbf.append(fname[index])
        hbl.append(lnanme[index])
    elif h_a[index] == "House Tully":
        ht += 1
        htf.append(fname[index])
        htl.append(lnanme[index])
    elif h_a[index] == "Night's Watch":
        nw += 1
        nwf.append(fname[index])
        nwl.append(lnanme[index])
    elif h_a[index] == "House Lannister":
        hl += 1
        hlf.append(fname[index])
        hll.append(lnanme[index])
    elif h_a[index] == "House Targaryen":
        hta += 1
        htaf.append(fname[index])
        htal.append(lnanme[index])
for index in range (0, len(fname)): #Adds total of all members and their ages.
    ttl += 1
    avga += age[index]
tavga = float(f"{avga/ len(fname):.0f}") #Takes total age and divdes by total number of names on list
print(f"{'Firstname':9}\t{'Lastname':9}\t{'Age':1}\t{'Nickname':18}\t{'House Allegiance':15}\t{'House Mottos'}") #Header
for index in range (0, len(fname)): #Index that prints total of everything
    print(f"{fname[index]:9}\t{lnanme[index]:9}\t{age[index]}\t{nick[index]:18}\t{h_a[index]:15}\t\t{h_m[index]:15}")

#Print lines for total, average age and each house members total amount and the first and last name of each house member
print(f"There are {ttl} people in this list of houses")
print(f"The average age of all houses is {tavga}")
print(f"There are {hs} members of House stark")
for i in range (0, len(hslf)):
    print(f"{hslf[i]} {hsll[i]}")
print(f"There are {hb} members of house Baratheon")   
for i in range (0, len(hbf)):
    print(f"{hbf[i]} {hbl[i]}")
print(f"There are {ht} members of House Tully")
for i in range (0, len(htf)):
    print(f"{htf[i]} {htl[i]}")
print(f"There are {nw} members of Night's Watch")
for i in range (0, len(nwf)):
    print(f"{nwf[i]} {nwl[i]}")
print(f"There are {hl} members of House Lannister")
for i in range (0, len(hlf)):
    print(f"{hlf[i]} {hll[i]}")
print(f"There are {hta} members of House Targaryen")
for i in range (0, len(htaf)):
    print(f"{htaf[i]} {htal[i]}")
