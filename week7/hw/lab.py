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
def id_search(id_search):

    found_index = ""

    for i in range(0, len(id)):

        if id[i] == id_search:

            found_index = i

    return found_index