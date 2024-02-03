#Chris Southey
#SE126 Intermidiate prog using Python
#Class Lab 4

#02-03-24

#Write a program that reads the data file (below) and stores the data into 1D parallel lists (remember, one list for every field).  Once the lists are populated (and the file is "closed"), process the lists to reprint the file data, record by record as they originally appear in the file.

#-----------------------------------------------
import csv

fname = []
lname = []
t1 = []
t2 = []
t3 = []

with open("week4/hw/listPractice1.txt") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:

        fname.append(rec[0])
        lname.append(rec[1])
        t1.append(int(rec[2]))
        t2.append(int(rec[3]))
        t3.append(int(rec[4]))

#Out of loop-------------------------
print("--------------------------------------------------------")
print(f"{'First':12} \t {'LAST':12} \t {'TEST1'} \t {'TEST2'} \t {'TEST3'}")
print("--------------------------------------------------------")

for i in range(0, len(fname)):

    print(f"{fname[i]:12} \t {lname[i]:12} \t {t1[i]} \t {t2[i]} \t {t3[i]}")
print("--------------------------------------------------------")

avg = 0
total_count = 0
average = []

for i in range(0, len(t1)):

    avg = (t1[i] + t2[i] + t3[i]) / 3

    average.append(avg)


print("\n---------------------------")
print(f"{'fname':12} \t {'average':8}")
print("---------------------------")
for i in range(0, len(fname)):

    print(f"{fname[i]:12} \t {average[i]:.1f}")

print("---------------------------")

let_avg = []
let = " "

for i in range(0, len(average)):

    
    if avg >= 90:
        let = "A"

    elif avg >= 80:
        let = "B"

    elif avg >= 70:
        let = "C"

    elif avg >= 60:
        let = "D"

    else:
        let = "F"


    let_avg.append(let)
 
 
print("\n---------------------------")
print(f"{'fname':12} \t {'average'} \t {'letter'}")
print("---------------------------")
for i in range(0, len(let_avg)):

    print(f"{fname[i]:12} \t {average[i]:.1f} \t {let}")




