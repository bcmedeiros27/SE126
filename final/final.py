import csv

rows = []
seatA = []
seatB = []
seatC = []
seatD = []
seatE = []
seatF = []
seatG = []
seatH = []
seatI = []
seatJ = []
seatK = []
seatL = []
seatM = []
seatN = []
seatO = []
seatP = []
seatQ = []
seatR = []
seatS = []
seatT = []
seatU = []
seatV = []
seatW = []
seatX = []
seatY = []
seatZ = []
seat1 = []
seat2 = []
seat3 = []
seat4 = []

with open("final/final.csv") as csvfile: #Basic csv reader
    file = csv.reader(csvfile)
    for rec in file:
        rows.append(rec[0])
        seatA.append(rec[1])
        seatB.append(rec[2])
        seatC.append(rec[3])
        seatD.append(rec[4])
        seatE.append(rec[5])
        seatF.append(rec[6])
        seatG.append(rec[7])
        seatH.append(rec[8])
        seatI.append(rec[9])
        seatJ.append(rec[10])
        seatK.append(rec[11])
        seatL.append(rec[12])
        seatM.append(rec[13])
        seatN.append(rec[14])
        seatO.append(rec[15])
        seatP.append(rec[16])
        seatQ.append(rec[17])
        seatR.append(rec[18])
        seatS.append(rec[19])
        seatT.append(rec[20])
        seatU.append(rec[21])
        seatV.append(rec[22])
        seatW.append(rec[23])
        seatX.append(rec[24])
        seatY.append(rec[25])
        seatZ.append(rec[26])
        seat1.append(rec[27])
        seat2.append(rec[28])
        seat3.append(rec[29])
        seat4.append(rec[30])


o = True
y = True
a = True
x = False
z = False
b = False
purchase = 0
seats = 0
def menu():
    print("1. Purchase Seat(s)")
    print("2. View Total Ticket Sales")
    print("3. View Sales Information")
    print("4. Checkout")
    print("5. Quit")

def purchase1(purchase):
    global a
    global b
    global y
    global z
    a = o
    b = x
    y = o
    z = x
    while a:
        try:
            seatrow = int(input("Enter the row number: "))
            if seatrow < 0 or seatrow > 15:
                print("Invalid row number. Please enter a number between 1 and 15.")
                a = a
            else:
                a = b
        except ValueError:
            print("Invalid row number. Please enter a numeric value.")
        
    
        
    while y:
        seat = input("Enter the seat column: ").lower()
        if seat.isalpha() and seat in ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]:
            y = z
        elif seat.isdigit() and seat in ['1', '2', '3', '4']:
            y = z
        else:
            print("Invalid seat column. Please enter a letter from A to Z or a number from 1 to 4.")
            y = y
    
            

    if seatrow >= 0 and seatrow < len(rows):
        if seat in seat_map:
            if seat_map[seat][seatrow] == "#":
                if seatrow < 6:
                    print("Seat purchased for $200.00")
                    purchase += 200.00
                elif seatrow < 11:
                    print("Seat purchased for $175.00")
                    purchase += 175.00
                else:
                    print("Seat purchased for $150.00")
                    purchase += 150.00
                print("Seat purchased")
                seat_map[seat][seatrow] = "*"
                global seats
                seats = seats + 1 
                return  purchase
                
            else:
                print("Seat not available")
                purchase = 0
                return purchase
                
        else:
            print("Invalid seat letter")
    else:
        print("Invalid row number") 
seat_map = {
        "a": seatA,
        "b": seatB,
        "c": seatC,
        "d": seatD,
        "e": seatE,
        "f": seatF,
        "g": seatG,
        "h": seatH,
        "i": seatI,
        "j": seatJ,
        "k": seatK,
        "l": seatL,
        "m": seatM,
        "n": seatN,
        "o": seatO,
        "p": seatP,
        "q": seatQ,
        "r": seatR,
        "s": seatS,
        "t": seatT,
        "u": seatU,
        "v": seatV,
        "w": seatW,
        "x": seatX,
        "y": seatY,
        "z": seatZ,
        "1": seat1,
        "2": seat2,
        "3": seat3,
        "4": seat4,
    }
purchase2 = 0
totalSeats = 0
while o:

    for i in range(len(rows)):
        print(f"{rows[i]:2} {' '.join(seat_map[letter][i] for letter in seat_map)}")
    print(f"Total seats purchased: {seats}\ntotal price: ${purchase2:.2f}")
    purchase = 0
    menu()
    choice = input("Enter your choice: ")
    if choice == "1":
        purchase = purchase1(purchase)
    elif choice == "2":
        print(f"Total seats purchsed: {seats}\ntotal price ${purchase2:.2f}")
        input("Press enter to continue")
    elif choice == "3":
        print("Sales Information")
        print("Number of seats sold: ", seats)
        print("Seats available in each row:")
        
        for i in range(1, len(rows)):
            print(f"{rows[i]}: {seat_map['a'][i].count('#') + seat_map['b'][i].count('#') + seat_map['c'][i].count('#') + seat_map['d'][i].count('#') + seat_map['e'][i].count('#') + seat_map['f'][i].count('#') + seat_map['g'][i].count('#') + seat_map['h'][i].count('#') + seat_map['i'][i].count('#') + seat_map['j'][i].count('#') + seat_map['k'][i].count('#') + seat_map['l'][i].count('#') + seat_map['m'][i].count('#') + seat_map['n'][i].count('#') + seat_map['o'][i].count('#') + seat_map['p'][i].count('#') + seat_map['q'][i].count('#') + seat_map['r'][i].count('#') + seat_map['s'][i].count('#') + seat_map['t'][i].count('#') + seat_map['u'][i].count('#') + seat_map['v'][i].count('#') + seat_map['w'][i].count('#') + seat_map['x'][i].count('#') + seat_map['y'][i].count('#') + seat_map['z'][i].count('#') + seat_map['1'][i].count('#') + seat_map['2'][i].count('#') + seat_map['3'][i].count('#') + seat_map['4'][i].count('#')}")
            totalSeats += seat_map['a'][i].count('#') + seat_map['b'][i].count('#') + seat_map['c'][i].count('#') + seat_map['d'][i].count('#') + seat_map['e'][i].count('#') + seat_map['f'][i].count('#') + seat_map['g'][i].count('#') + seat_map['h'][i].count('#') + seat_map['i'][i].count('#') + seat_map['j'][i].count('#') + seat_map['k'][i].count('#') + seat_map['l'][i].count('#') + seat_map['m'][i].count('#') + seat_map['n'][i].count('#') + seat_map['o'][i].count('#') + seat_map['p'][i].count('#') + seat_map['q'][i].count('#') + seat_map['r'][i].count('#') + seat_map['s'][i].count('#') + seat_map['t'][i].count('#') + seat_map['u'][i].count('#') + seat_map['v'][i].count('#') + seat_map['w'][i].count('#') + seat_map['x'][i].count('#') + seat_map['y'][i].count('#') + seat_map['z'][i].count('#') + seat_map['1'][i].count('#') + seat_map['2'][i].count('#') + seat_map['3'][i].count('#') + seat_map['4'][i].count('#')

        print("Total seats available: ", totalSeats)
        totalSeats = 0
        input("Press enter to continue")
    elif choice == "4":
        if purchase2 == 0:
            print("No purchase made")
            print("returning to menu")
        else:
            print("Checkout")
            payOut = int(input(f"your total is ${purchase2:.2f} Please enter amount you wish to pay:"))
            payTotal = payOut - purchase2
            if payTotal < 0:
                print("You have not paid enough get more cash")
            else:
                print(f"Your change is ${payTotal:.2f}")
                purchase2 = 0
                seats = 0
                totalSeats = 0
        input("Press enter to continue")
    elif choice == "5":
        print("Quit")
        o = x
    else:
        print("Invalid choice")
        input("Press enter to continue")
    purchase2 += purchase

for i in range(len(rows)):
    print(f"{rows[i]:2} {' '.join(seat_map[letter][i] for letter in seat_map)}")
