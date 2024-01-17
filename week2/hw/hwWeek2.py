import csv

total_records = 0

with open("week2/hw/lab2b.csv") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:

        #variables for each field
        #-----values for rec[0]-----
        if rec[0] == "D":
            comp_type = "Desktop"
        elif rec[0] == "L":
            comp_type = "Laptop"
        else:
            comp_type = "-Error-"

        #-----values for rec[1]-----
        if rec[1] == "DL":
            manu = "Dell"
        elif rec[1] == "GW":
            manu = "Gateway"
        elif rec[1] == "HP":
            manu = rec[1]
        else:
            manu == "-Error-"
        
        #-----values for rec[2] - rec[5]-----
        processor = rec[2]
        ram = rec[3]
        hdd_1 = rec[4]
        num_hdd = rec[5]


        #final printed message for each machine
        print(rec)
        print(f"{comp_type} {manu} {processor} {ram} {hdd_1} { num_hdd} {hdd_2} {os} {year}")

