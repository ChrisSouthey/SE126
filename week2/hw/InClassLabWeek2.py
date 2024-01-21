#Chris Southey
#SE126 Intermidiate prog using Python
#Class Lab 1

#01-19-23

#Write a program that displays all rooms that are over the maximum limit of people and the number ofpeople that have to be notified that they will have to be put on the wait list.

#-----------------------------------------------

import csv

total_records = 0
overcomp = 0

with open("week2/hw/lab2a.csv") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:

        names = rec[0]
        comp = int(rec[1])
        attend = int(rec[2])

        total_records += 1

        if attend > comp:

            overcomp += 1

            over = attend - comp
            print("\nRoom\t\tCompacity\tAttending\tOver")
            print(f"{names:.7}\t\t{comp}\t\t{attend}\t\t{over}")
            #i had so many problems getting this to allign correctly 0_0

    print(f"\n{total_records} records processed")
    print(f"{overcomp} rooms will be over compacity\n")

    

            



