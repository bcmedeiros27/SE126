#var list
row = [1,2,3,4,5,6,7]
seata = ["A","A","A","A","A","A","A"]
seatb = ["B","B","B","B","B","B","B"]
seatc = ["C","C","C","C","C","C","C"]
seatd = ["D","D","D","D","D","D","D"]
#def list --------


def term():
    for i in range(0, len(row)):
        print(f"{row[i]}\t\t{seata[i]} {seatb[i]}\t\t{seatc[i]} {seatd[i]}")
allFlight = []
for i in range(0, len(row)):
    allFlight.append([row[i], seata[i], seatb[i], seatc[i], seatd[i]])
#print(allFlight)

def display ():
    for i in range(0, len(allFlight)):
        for x in range(0, len(allFlight[i])):
            print(f"{allFlight[i][x]:} ", end="") #Final index print statment
        
        print()

O = True
X = False
while O == O:

    useR = int(input("enter:"))-1
    useS = (input("enter")).upper()
    useSS = ""
    if useS == "A":
            useSS = 1
    if useS == "B":
            useSS = 2
    if useS == "C":
            useSS = 3
    if useS == "D":
            useSS = 4
    if allFlight[useR][useSS] == "X":
            print(f"Error: Row {useR} and  Seat {useS} already occupied.")
    else:
        allFlight[useR][useSS] = "X"
    if allFlight[useR][useSS] == allFlight[useR][useSS]:
            allFlight[useR][useSS] = "X"
    display()

        