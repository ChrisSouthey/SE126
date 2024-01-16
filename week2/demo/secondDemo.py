#import csv library
import csv

#initialize counting vars
total_records = 0
total_salaries = 0

#initialize empty lists -  1 list per field
names = []
ages = []
salaries = []

#connect to the file
with open("week2/demo/example.csv") as csvfile:

    #read the file
    file = csv.reader(csvfile)

    #go in and read each record in the file
    for rec in file:
        #for every record in the file (entire row of field data)

        #display the data VALUES in NEAT columns
        print(f"{rec[0]:10} \t{rec[1]:3} \t${rec[2]:10}")

        #store data from rec list (current record being read) to list
        #adding data to a list --> .append() ; requires LIST NAMES as starting objects
        names.append(rec[0]) #NAME
        ages.append(int(rec[1])) #age
        salaries.append(float(rec[2])) #SALARY

        #keep literal count of number of records
        total_records += 1

        #kep running total of salaries
        total_salaries += float(rec[2])

#final total displays
print(f"TOTAl records: {total_records} | TOTAL SALARIES: ${total_salaries:.2f}")

#process the lists to display the text file information
#PROCESS LIST --> FOR LOOP!
for index in range(0, total_records):
    #for each value in the range of 0 to total umber of values in total_records
    print(f"INDEX: {index} \t {names[index]} is {ages[index]} years old")

#process through the list to create a total age value
total_age = 0

for index in range(0, total_records):
    #add each age to a total age variable
    total_age += ages[index]
#determine the average age, then display
average_age = total_age / total_records
print(f"AVERAGE AGE:{average_age:.2f} ")