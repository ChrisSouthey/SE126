import csv

#creat 1D lists [will be parallel to each other]
#base lists on fields in file

fname = []
lname = []
test1 = []
test2 = []
test3 = []

#connect to a file and read data into 1D lists
with open("week4/demo/files/listPractice1-1.txt") as csvfile:

    file = csv.reader(csvfile)

    #come back and show print(file) later

    for rec in file:
        #store data from file fields to their respective lists
        #by PARALLEL - storing initial file record data at same position (index) in each list --> use the same data [INDEX] across each list to find "matching" data
        fname.append(rec[0])
        lname.append(rec[1])
        test1.append(int(rec[2])) #cast as int for math
        test2.append(int(rec[3]))
        test3.append(int(rec[4]))
#disconnect from file -------------------------

#PROCESS the lists --> for loop
#display the file data
print(f"{'First':12} \t {'LAST':12} \t {'TEST1'} \t {'TEST2'} \t {'TEST3'}")
print("--------------------------------------------------------")
for i in range(0, len(fname)): 
    #len() --> returns LENGTH of (item) -> for lists, it is the # of items in the list

    print(f"{fname[i]:12} \t {lname[i]:12} \t {test1[i]} \t {test2[i]} \t {test3[i]}")
print("--------------------------------------------------------")

#calculate and store each students AVERAGE TEST SCORE
avg = 0
total_count = 0
average = []

for i in range(0, len(test1)):

    #calculate average for student
    avg = (test1[i] + test2[i] + test3[i]) / 3

    #append this average to the avergage[]
    average.append(avg)

#display students fname and test average
print(f"{'FIRST'} \t {'AVERAGE'}")
for i in range(0, len(fname)):
    print(f"{fname[i]:12} \t {average[i]:8.1f}")

#SEQUENTIAL SEARCH - "in sequence" --> from beggining THROUGH the end
low_name = ""
low_avg = 100 #start with highest valueto drop to find lowest

for i in range(0, len(average)):

    #determine if current average is lower than current low_avg
    if average[i] < low_avg:

        low_avg = average[i] #current average is lower, so becomes new low value
        low_name = fname[i]



#DISPLAY: total students in file
print(f"STUDENTS IN FILE: {len(fname)}")
print(f"LOWEST AVERAGE: {low_name} - {low_avg:.1f}")

#----2D lists------------------------------------------------------------------------------
#use your 1D lists to populate a new, 2D list
all_students = []

for i in range(0, len(fname)):

    #add each students data to their (index) place in the all_students[]
    all_students.append([fname[i], lname[i], test1[i], test2[i], test3[i], average[i]])

#display the 2D list to the console - for now, just get the lists to display ie ['Floyd', 'Eastham', '100', '85', '93']
for i in range(0, len(all_students)):
    print(f"{all_students[i]}")

print(f"----2D lists - INDIV. VALUES!--------------------------------")
print(f"{'First':12} \t {'LAST':12} \t {'TEST1'} \t {'TEST2'} \t {'TEST3'} \t {'AVERAGE'}")
print("---------------------------------------------------------------------------")
#display the 2D list to the console where each value for each list appears as a value (and not a list item)
for i in range(0, len(all_students)):
    #we have lists within a list - outter for handles main list (all_students)
    for x in range(0, len(all_students[i])):
        #inner for handles each value found at current list (all_students[i])
        print(f"{all_students[i][x]}", end="")

    #include an extra empty print() to cancle the interior print's end=""
    print()