#W5D1 - 1D List Review + Function Review + Sequential Search

import csv

fname = []
lname = []
test1 = []
test2 = []
test3 = []

#to be created
num_avg = []
let_avg = []

#-----FUNCTIONS------------------------------------------

def menu():

    print("~CLASS ACCOUNT MENU~")
    print("1. Show All Atudents")
    print("2. Show Roster Only")
    print("3. Search for a Student")
    print("4. EXIT")

    choice = int(input("Enter your choice [1 - 4]: "))

    #loop trap the user if the dont follow directions
    while choice != 1 and choice != 2 and choice != 3 and choice != 4:
        print("\n\t\t***ERROR***")
        choice = int(input("Enter your choice [1 - 4]: "))

    return choice


def seq_search(search_term):

    #search_term is a local var name and only exists in this def block

    #initialize found_index var
    found_index = "" #set as empty

    #SEQUENTIAL SEARCH - "In sequence" -> start @ beggining (0) go to the end (len(listName))
    for i in range(0, len(lname)):

        #look at each value in a list to find what your looking for
        if lname[i] == search_term:
            found_index = i

    return found_index

#-----FILE CONNECTION/LIST POPULATION--------------------
with open("week5/demo/listPractice1.txt") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:

        fname.append(rec[0])
        lname.append(rec[1])
        test1.append(int(rec[2]))
        test2.append(int(rec[3]))
        test3.append(int(rec[4]))
#Out of loop
print(f"{'FIRST':12} \t{'LAST':12} \t {' T1':4} \t {' T2':4} \t {' T3':4} \t {'AVG':5} \t{'LETTER':3}")
print("--------------------------------------------------------------------")

#populate additional lists - num_avg and let_avg
for i in range(0, len(lname)):
    avg= (test1[i] + test2[i] + test3[i]) /3
    num_avg.append(avg)

    if avg >= 90:
        letter = "A"

    elif avg >= 80:
        letter = "B"

    elif avg >= 70:
        letter = "C"

    elif avg >= 60:
        letter = "D"

    elif avg < 60:
        letter = "F"

    else:
        letter = "ERROR @ I:" + str(i)

    let_avg.append(letter)




for i in range(0, len(lname)):
    print(f"{fname[i]:12} \t{lname[i]:12} \t{test1[i]:4} \t{test2[i]:4} \t{test3[i]:4} \t{num_avg[i]:5.1f} \t{let_avg[i]:3}")

#-----MAIN CODE------------------------------------------



#Allow a user to choose an option from a menu and display certain data
#user will repeatedly see the menu until they choose to exit


#show user menu, store into a var, use the var for the loop
menu_choice = menu()

while menu_choice != 4: #4 means exit

    #determine what user wants to do
    if menu_choice == 1:
        print("\n\t--Showing all file data-----")

    elif menu_choice == 2:
        print("\n\t--Showing class roster-----")

    else: #choice 3
        print("\n\t--Search for a student-----")

        search = input("Enter the LAST name you are looking for: ")

        found = seq_search(search)

        if found != "":
            #display results to user
            print(f"{fname[found]:12} \t{lname[found]:12} \t{test1[found]:4} \t{test2[found]:4} \t{test3[found]:4} \t{num_avg[found]:5.1f} \t{let_avg[found]:3}")

        else: #found -- "" --> it never changed --> NOT FOUND
            print(f"The student {search} could not be found")

    #give user opportunity to see/reselect, or exit
    #breking out of the loop
    menu_choice = menu()

print("\n\n\tThanks for using the program. Goodbye!")

input("\n\n\nenter to continue....")