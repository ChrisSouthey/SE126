import csv

total_records = 0
print("Type\t\tBrand\t\tCPU\t\tRAM\t\t1st Disk\t # HDD\t\t2nd Disk\tOS\tYEAR")
print("-------------------------------------------------------------------------------------------------------------------------------")
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
        os = rec[6]
        year = rec[7]
    
        if num_hdd == "1":
            hdd_2 = ""

        elif num_hdd == "2":
            hdd_2 = rec[6]
            os = rec[7]
            year = rec[8]
        
        


        #final printed message for each machine
        
        print(f"{comp_type:<15} {manu:<15} {processor:<15} {ram:<15} {hdd_1:<16} {num_hdd:<14} {hdd_2:<15} {os:<7} {year}")

