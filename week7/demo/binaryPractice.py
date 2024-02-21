#W7D2 - Bubble sort and Binary search 
import csv

#create empty 1D lists
type = []
name = []
meaning = []
origin = []

with open("week7/demo/party.csv", encoding="utf-8") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:
        type.append(rec[0])
        name.append(rec[1])         #what we will sort and search by
        meaning.append(rec[2])
        origin.append(rec[3])

#original file print
print("---ORIGINAL FILE--------------------------------------------------------------")
print(f"{'TYPE':8} {'NAME':12} {'MEANING':30} \t{'ORIGIN'}")
for i in range(0, len(type)):
    print(f"{type[i]:8} {name[i]:12} {meaning[i]:30} \t{origin[i]}")
print("---ORIGINAL FILE--------------------------------------------------------------")


#sort the file data by first name, asending (increasing) order
#BUBBLE SORT----------------------------------------------------

for i in range(0, len(name) - 1):#outter loop

    for index in range(0, len(name) - 1):#inner loop

        #below if statement determines the sort

        #list used is the list being sorted

        # > is for increasing order, < for decreasing

        if(name[index] > name[index + 1]):

            #if above is true, swap places!
            temp = name[index]
            name[index] = name[index + 1]
            name[index + 1] = temp

 
            #swap all other values
            #--type--------
            temp = type[index]
            type[index] = type[index + 1]
            type[index + 1] = temp


            #--meaning--------
            temp = meaning[index]
            meaning[index] = meaning[index + 1]
            meaning[index + 1] = temp


            #--origin--------
            temp = origin[index]
            origin[index] = origin[index + 1]
            origin[index + 1] = temp

print("---SORTED FILE--------------------------------------------------------------")
print(f"{'TYPE':8} {'NAME':12} {'MEANING':30} \t{'ORIGIN'}")
for i in range(0, len(type)):
    print(f"{type[i]:8} {name[i]:12} {meaning[i]:30} \t{origin[i]}")
print("---SORTED FILE--------------------------------------------------------------")
#create a lop for user to repeatedly search through
#perform binary search
#BINARY SEARCH--------------------------------------------------
answer = "y"
while answer.lower() == "y":

    search = input("\nEnter name of Dragon: ").lower()

    min = 0
    max = len(name) - 1       #can also use len(listName) for 'records' value
    mid = int((min + max) / 2)


    #this is for INCREASING order
    while (min < max and search.lower() != name[mid].lower()):

        if search < name[mid]:
            max = mid - 1
        else:
            min = mid + 1

        mid = int((min + max) / 2)

    if search.lower() == name[mid].lower():
        #found them! use 'mid' for index of found search item
        print(f"\n\tWe found {search}! Here is their info:")
        print(f"{'TYPE':8} {'NAME':12} {'MEANING':30} \t{'ORIGIN'}")
        print(f"{type[mid]:8} {name[mid]:12} {meaning[mid]:30} \t{origin[mid]}")

    else:
        #boooo not found
        print(f"\n\tWe did not find {search}! Try again :)")


    answer = input("Would you like to search again? [y/n]: ")