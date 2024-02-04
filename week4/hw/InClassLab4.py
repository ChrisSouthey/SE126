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

#-----Getting average score------------------------
avg = 0
total_count = 0
average = []

for i in range(0, len(t1)):

    avg = (t1[i] + t2[i] + t3[i]) / 3.0

    average.append(avg)


print("\n---------------------------")
print(f"{'fname':12} \t {'average':8}")
print("---------------------------")
for i in range(0, len(fname)):

    print(f"{fname[i]:12} \t {average[i]:.1f}")

print("---------------------------")

#-----Getting letter grade---------------------------
let_avg = []
let = " "

for i in range(0, len(average)):

    #This part gave me so many problems
    avg = average[i]

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
 
 
print("\n-------------------------------------------")
print(f"{'fname':12} \t     {'average':8} \t {'letter'}")
print("-------------------------------------------")

for i in range(0, len(let_avg)):
    print(f"{fname[i]:12} \t {average[i]:8.1f} \t {let_avg[i]}")

print("-------------------------------------------")

#-----2D list------------------------

all_students = []

for i in range(0, len(fname)):

    all_students.append([fname[i], lname[i], t1[i], t2[i], t3[i], "%.1f"%average[i], let_avg[i]])

#for i in range(0, len(all_students)):
    #print(f"{all_students[i]}")


print("\n----------------------------------------------------------------------------------------------------------")
print(f"{'First':8}\t {'LAST':8} \t      {'TEST1':10}       {'TEST2':8}       {'TEST3':8}   {'AVERAGE':10} \t {'Letter'}")
print("----------------------------------------------------------------------------------------------------------")

for i in range(0, len(all_students)):

    for x in range(0, len(all_students[i])):

        print(f"{all_students[i][x]:8}", end="\t ")

    print()

print("----------------------------------------------------------------------------------------------------------\n")