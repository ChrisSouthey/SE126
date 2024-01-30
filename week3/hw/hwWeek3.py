#Chris Southey
#SE126 Intermidiate prog using Python
#Lab 3

#01-29-24

#Construct a program that will analyze potential voters.

#-----------------------------------------------
import csv

#creating empty variables
total_records = 0
not_elig = 0
no_reg = 0
elig_no_vote = 0
did_vote = 0


print(f"{'id#':6} {'age':6} {'voted':8} {'registered'}")
print("----------------------------------")

with open("week3/hw/voters_202040.csv") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:

        #storing values to lists
        id = rec[0]
        age = rec[1]
        registered = rec[2]
        vote = rec[3]

        #print(rec)
        print(f"{id:6} {age:6} {vote:8} {registered}")

        total_records += 1

        #getting numbers n stuff
        if int(age) < 18:
            not_elig += 1
        
        elif int(age) >= 18 and registered == "N":
            no_reg += 1

        elif registered == "Y" and vote == "N":
            elig_no_vote += 1

        elif vote == "Y":
            did_vote += 1




print("----------------------------------")
#print(not_elig, no_reg, elig_no_vote, did_vote, total_records)

print(f"{total_records} records processed")
print(f"\n{not_elig} records are not eligible to vote")
print(f"{no_reg} records are of age but not registered to vote")
print(f"{elig_no_vote} records are eligible to vote but did not")
print(f"{did_vote} records did vote\n")

