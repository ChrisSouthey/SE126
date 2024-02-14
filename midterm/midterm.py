import csv

#Chris Southey
#Midterm project
#The user will see a printed list of famous guitarists, the band they are in, Their signature guitar, and the average price of that guitar, and be able to search for a specific guitarist

#-----Lists-----------------------------------------
name = []
band = []
guitar = []
price = []



#-----Functions-------------------------------------
def menu():
    print("\n\t\tWelcome")
    print("\t1. Show all Guitarists")
    print("\t2. Show only Guitarists")
    print("\t3. Show Only Guitars")
    print("\t4. Search by Guitarists")
    print("\t5. Exit")
    

    choice = input("\tEnter your Choice [1 - 5]: ")
    
    print("")

    while choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5":
        print("\n\t\t***ERROR***")
        
        choice = input("\n\tEnter your Choice [1 - 5]: ")
        

    return choice


def seq_search(name_search):

    found_index = ""

    for i in range(0, len(name)):

        if name[i] == name_search:

            found_index = i

    return found_index



#-----loop-----------------------------------------


with open("midterm/MidtermList.txt") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:

        if len(rec) != 4:
            name.append(rec[0])
            band.append("   ")
            guitar.append(rec[1])
            price.append(int(rec[2]))
        
        else:
            name.append(rec[0])
            band.append(rec[1])
            guitar.append(rec[2])
            price.append(int(rec[3]))

        #print(rec)

menu_choice = menu()


while menu_choice != "5":

    if menu_choice == "1": #Showing all records
        print(f"{'NAME':18} \t {'BAND':24} \t {'GUITAR':31} \t {'PRICE':9}")
        print("-------------------------------------------------------------------------------------------------------------")
        for i in range(0, len(name)):
            print(f"{name[i]:15} \t {band[i]:25} \t {guitar[i]:30} \t ${price[i]:9.2f}")

        print("-------------------------------------------------------------------------------------------------------------\n")
        menu_choice = menu()

    if menu_choice == "2": #Showing first 2 fields
        print(f"{'NAME':18} \t {'BAND':24}")
        print("--------------------------------------------")
        for i in range(0, len(name)):
            print(f"{name[i]:15} \t {band[i]:25}")

        print("--------------------------------------------\n")
        menu_choice = menu()

    if menu_choice == "3": #Showing last 2 fields
        print(f"{'GUITAR':35} \t {'PRICE':9}")
        print("------------------------------------------------------")
        for i in range(0, len(name)):
            print(f"{guitar[i]:35} \t ${price[i]:9.2f}")

        print("------------------------------------------------------\n")
        menu_choice = menu()

    if menu_choice == "4": #Search by name
        search = input("\nEnter the NAME of the guitarist you are searching for: ")

        found = seq_search(search)

        if found != "":
            print(f"{'NAME':18} \t {'BAND':24} \t {'GUITAR':31} \t {'PRICE':9}")
            print("-------------------------------------------------------------------------------------------------------------")
            print(f"{name[found]:15} \t {band[found]:25} \t {guitar[found]:30} \t ${price[found]:9.2f}")

        else:
            print(f"Could not find {search} in the list, either you misspelled the name or they are not in the list.")

        menu_choice = menu()

    
print("Thank you for using this program. Have a nice day and Rock on!")





