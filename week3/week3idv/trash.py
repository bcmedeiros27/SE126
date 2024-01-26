import csv
total_records = 0
ss = []
ssct = 0
age = []
unelg = 0
old_y = []
old_n = []
yng_n = []
vot = []
env = []
edv = []

with open ("week3/week3idv/voters_202040.csv") as csvfile:
    file = csv.reader(csvfile)
    for rec in file:
        ss.append(rec[0])
        ssct += 1
        age.append(rec[1])
        if int(rec[1]) >= 18:
            if rec[2] == "Y":
                old_y.append(rec[2])
                old_n.append("")
            else:
                old_n.append(rec[2])
                old_y.append("")
        if rec[2] == "Y":
            if int(rec[1]) >= 18:
                if rec[3] == "N":
                    env.append(rec[3])
                else:
                    edv.append(rec[3])

        if int(rec[1]) <= 17:
            yng_n.append(rec[2])
            
            old_y.append("")
            old_n.append("")
            unelg += 1
    total_records +1
print (f"{old_y}{old_n}{yng_n}[count {unelg}]{env}{edv}")
print(f"{'NER':4} {'OldDNR':6} {'EDNV':3} {'Votes':3} {'records':5}")
for index in range(0, (ssct)):
    if yng_n <=  old_y:
        yng_n.append(old_y[index])

print(f"{yng_n} {old_y} {old_n}")
# count = 0
# for index in range(0, len(ss)):
#        print("1")
#        count += 1
# print(f"{count}")
            