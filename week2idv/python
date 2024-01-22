#Brandon Medeiros
#Lab 2 individual
#1/22/24
#you have been asked to produce a report that lists all the computers in the csv file lab2b.csv. Your
#report should look like the following sample output. The last line should print the number of
#computers in the file.
################################################################
#variable dictonary
#total_records = 0 ct of records
#desktop = [] desktop list
#laptop = [] Laptop list
#brand = [] Brand of the computer
#cpu = [] #cpu list
#ram = [] #ram list
#gb = [] Drive list size
#drive = [] Drive
#drive_type = [] Second drives
#os = [] Operating system
#yr = [] Year of the computer
import csv
total_records = 0 #keeps count
desktop = [] #lists desktops. could have listed laptops to but i was still learning. later used one list
laptop = [] #laptops list, old way of doing things made two lists but found out how to merge
brand = [] #brand of the pc. Hey do you realllly read these??? if so I'll hide more jokes
cpu = [] #cpu list, i'll explain more in the fore loop
ram = [] #ram list, 
gb = [] #gb list
drive = [] #list of the drive
drive_type = [] #list of second drives
os = [] #operating system
yr = [] # year
#pv1 = desktop #old variable i used to check files. 
with open("week2idv/lab2b.csv") as csvfile: 
    file = csv.reader(csvfile) #basic csv file and for loop
    
    for rec in file: #basic for loop. read all the records in file and lists them
        total_records += 1
        if rec[0] == "D" and rec[0] != "L": #checks record 0 for a D to be true and L to be flase
            desktop.append("desktop") #appends to the desktop var
        elif rec[0] == "L" and rec[0] != "D": #checks record 0 for a L to be true and D to be flase.
            desktop.append("laptop") #appends to the desktop again. creating a basic list for an index later
        
        if rec[1] == "DL" or rec[1] is None: #it took me a while but i figured I could just call the rec[0] itself. This worked but was sloppy
            brand.append("DELL") #adding the brand to the list
        elif rec[1] == "HP": #elif for breands
            brand.append("HP") #elif for brands
        elif rec[1] == "GW":#elif for brands
            brand.append("GW") #elif for brands
        if rec[2] == "i5" or rec[2] is None: #again same idea as Rec[1] trying to match the records instead of calling them. makes more work
             cpu.append("i5") #elif for cpu
        elif rec[2] == "i7": #elif for cpu
             cpu.append("i7") #elif for cpu
        if rec[3] == "08": #still the same idea. found something that worked and keept on going with it
             ram.append("08") #elif for ram
        elif rec[3] == "16": #elif for ram
            ram.append("16") #elif for ram
        if rec[4] == "001TB": #still the same idea. added much more statments then needed,
             gb.append("001TB") #elif for gb
        elif rec[4] == "500GB": #elf for gb
             gb.append("500GB") #elif for gb
        if rec[5] == "1": #again more of the same idea.
             drive.append("1") #elif for drive
        elif rec[5] == "2": #elif for drive 
             drive.append("2")#elif for drive
        if len(rec) == 9: #heres where I ran into trouble. I could no longer really on the list as its order was out. Figured out how to call certan parts of the list and check them for what i needed. from here I am apple to append my list with the record
             drive_type.append(rec[6]) #appends record 6 for the missing lines.
        else:
             drive_type.append("") #an empty string for record 6.
        if len(rec[6]) == 3: # record 6 has both the GB and Windows. in order to isolate them I checked the len of windows and appened that to the OS variable using record
             os.append(rec[6]) #appened variable. I am now figuring out how to modify and apend variables with diffrent records
        if len(rec[7]) == 3: #from here I keep up the same pratice. I am learning how to modify and append variables to be much eaiser and cleaner to use
             os.append(rec[7]) #same idea as before. check the len and call the record to what i need. place it in a variable list i can call later
        if len(rec) == 9: #same idea as before I finally have a good grasp of what I want to do
             yr.append(rec[8]) #uses the same logic as last time to append and make variables
        else:
             yr.append(rec[7]) #last one! YAY!
        # if len(rec[8]) == 2:
        #      yr.append(rec[8])
        # if len(rec[7]) == 2:
        #      yr.append(rec[7]) Old code. took me a while to get the hand of things

        
        
        
        
             


       
             
        
             
        
        

print("Type\t Brand\t Cpu\t Ram\t 1st Disk  No. Hdd\t2d Disk\t\t Os\tYr") #Header for terminal. I'm still terrible at this
for index in range(0, len(desktop)): #checks an index in the desktop range. this creates a baseline list for me to work out of and test
             
            print (f"{desktop[index]:1}\t {brand[index]:1}\t {cpu[index]:1}\t {ram[index]:1}\t {gb[index]:1}\t    {drive[index]:0}\t\t{drive_type[index]:0}\t\t {os[index]:1}\t{yr[index]:1}") #the print statment with everything organized. Its bassicly trial and error if i get this to look good.
#pv1 = desktop
#pv2 = laptop
#print(f"{pv1}")
#print(f"{pv2}")
print(f"\nthere are {total_records} computer records")
print("\n\ngoodbye")

        

