#W2D2 - Text file opeining review + 1D lists

import csv

total_records = 0

#creat empy list for each field
fnames = []
lnames = []
favnums = []
favanimals = []

with open("week2/demo/w2d2_demoTextFile.txt") as csvfile:
    #we must indent when connected to and reading the file
    
    file = csv.reader(csvfile)

    for rec in file:

        print(rec)

        #append field data to the approptiate list(s)
        fnames.append(rec[0])
        lnames.append(rec[1])
        favnums.append(int(rec[2]))

        #len() --> returns length of a structure (list);
        #the maximum length of rec is: 4

        if len(rec) == 4:


            favanimals.append(rec[3])
        else: #rec[3] does not exist
            favanimals.append("---")

#process fnames + favanimals list to display
for index in range(0, len(fnames)):
    print(f"{fnames[index]}'s fave animal is {favanimals[index]}!")



