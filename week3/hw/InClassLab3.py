#Chris Southey
#SE126 Intermidiate prog using Python
#Class Lab 3

#01-28-24

#produce an end report that lists the number of desktops that will be replaced, the cost to replace the desktops, the number of laptops that will be replaced, and the cost to replace the laptops.

#-----------------------------------------------
import csv

total_records = 0
outdated = 0
lap = 0
desk = 0

print(f"{'TYPE':8} {'MANU':8} {'PROC':6} {'RAM':6} {'HDD1':6} {'#HDD':6} {'HDD2':6} {'OS':6} {'YEAR':6}")
print("-----------------------------------------------------------------")
with open("week3/hw/lab3a.csv") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:

        #storing values to lists
        comp_type = rec[0]
        manu = rec[1]
        processor = rec[2]
        ram = rec[3]
        hdd_1 = rec[4]
        num_hdd = rec[5]

        if rec[5] == "1":
            hdd_2 = "   "
            os = rec[6]
            year = rec[7]


        elif rec[5] == "2":
            hdd_2 = rec[6]
            os = rec[7]
            year = rec[8]


        #Getting the number of devices that need to be replaced
        if int(year) <= 16 and comp_type == "D":
            outdated += 1
            desk += 1

        elif int(year) <= 16 and comp_type == "L":
            outdated += 1
            lap += 1 

        print(f"{comp_type:8} {manu:8} {processor:6} {ram:6} {hdd_1:6} {num_hdd:6} {hdd_2:6} {os:6} {year:6}")


#outside loop
#print(outdated)
#print(desk)
#print(lap)

desk_cost = desk * 2000
lap_cost = lap * 1500

#Final print statement
print(f"\n{outdated} total devices need to be replaced")
print(f"\nTo replace {desk} desktops it will cost: ${desk_cost:6}")
print(f"To replace {lap} laptops it will cost:  ${lap_cost:6}\n")

