import csv

#Chris Southey
#SE126 Intermidiate prog using Python
#Lab 5

#03-03-24

#In this lab, you will build a Python application that allows a user to repeatedly choose an option from a menu to search through the data provided in the text file below. You will perform both sequential search as well as binary search. See the lab prompt for further details. 

#-----Lists--------------------

id = []
lname = []
fname = []
class1 = []
class2 = []
class3 = []
found_class = []

#-----Functions----------------
def menu():
    print("\nWelcome to the Student Reviewer Program")
    print("1. See all Reports")
    print("2. Search for Student by ID")
    print("3. Search for Student by Last Name")
    print("4. View a Class Roster")
    print("5. Exit")

    choice = input("\nEnter your selection [1-5]: ")

    print("")

    while choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5":
        print("\n\t\t***ERROR***")
        
        choice = input("\n\tEnter your Choice [1 - 5]: ")
        

    return choice

#Search by ID
def id_search(id_search):

    found_index = ""

    for i in range(0, len(id)):

        if id[i] == id_search:

            found_index = i

    return found_index

#Search by Last Name
def num_search(id_search):

    found_index = ""

    for i in range(0, len(id)):

        if id[i] == id_search:

            found_index = i

    return found_index

#Search by Last Name
def name_search(lname_search):

    found_index = ""

    for i in range(0, len(lname)):

        if lname[i] == lname_search:

            found_index = i

    return found_index

#Search by Class
def class_search(classSearch):

    found_index = ""

    for i in range(0, len(class1)):

        if class1[i] == classSearch or class2[i] == classSearch or class3[i] == classSearch:

            found_index = i
            found_class.append(found_index)
    return found_index



#-----Main loop-----------------------------------
with open("week7/hw/lab5_students.txt") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:

        id.append(rec[0])
        lname.append(rec[1])
        fname.append(rec[2])
        class1.append(rec[3])
        class2.append(rec[4])
        class3.append(rec[5])

        #print(rec)

menu_choice = menu()

while menu_choice != "5":

    if menu_choice == "1":
        print(f"{'ID'} \t {'LAST':12}  {'FIRST':8}  {'CLASS1'}  {'CLASS2'}  {'CLASS3'}")
        print("---------------------------------------------------------")
        for i in range(0, len(lname)):
            print(f"{id[i]} \t {lname[i]:12}  {fname[i]:8}  {class1[i]} \t {class2[i]} \t {class3[i]}")
        print("---------------------------------------------------------")

        menu_choice = menu()

    if menu_choice == "2":
        search = input("\nEnter the ID# for the student you are searching for: ")

        found = id_search(search)

        if found != "":
            print(f"{'ID'} \t {'LAST':12}  {'FIRST':8}  {'CLASS1'}  {'CLASS2'}  {'CLASS3'}")
            print("---------------------------------------------------------")
            print(f"{id[found]} \t {lname[found]:12}  {fname[found]:8}  {class1[found]} \t {class2[found]} \t {class3[found]}")
            print("---------------------------------------------------------")
            
        else:
            print(f"**ERROR** Could not find a student with the ID: {search}")

        menu_choice = menu()

    if menu_choice == "3":
        search = input("\nEnter the LAST NAME for the student you are searching for: ")

        found = name_search(search)

        if found != "":
            print(f"{'ID'} \t {'LAST':12}  {'FIRST':8}  {'CLASS1'}  {'CLASS2'}  {'CLASS3'}")
            print("---------------------------------------------------------")
            print(f"{id[found]} \t {lname[found]:12}  {fname[found]:8}  {class1[found]} \t {class2[found]} \t {class3[found]}")
            print("---------------------------------------------------------")

        else:
            print(f"**ERROR** Could not find a student with the Last Name: {search}")

        menu_choice = menu()

    if menu_choice == "4":
        search = input("\nEnter the CLASS you wish to see the roster for: ").upper()

        found = class_search(search)
        found_class.append(found)
        if found != "":
            print(f"{'ID'} \t {'LAST':12}  {'FIRST':8}")
            print("---------------------------------------------")
            for i in range(0, len(found_class)):
                print(f"{id[found]} \t {lname[found]:12}  {fname[found]:8}")
            print("---------------------------------------------")

        else:
            print(f"**ERROR** Could not find Class by the name of: {search}")

    menu_choice = menu()
   