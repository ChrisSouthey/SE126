import csv
import os
from time import sleep

#Chris Southey
#Midterm project
#The user will see a printed list of famous guitarists, the band they are in, Their signature guitar, and the average price of that guitar, and be able to search for a specific guitarist


#note for KT: clear() issue, so using os.system('cls')
#-----Lists-----------------------------------------
name = []
age = []
dOrA = []
band = []
guitar = []
price = []




#-----Functions-------------------------------------
def menu(): #Menu func
    print("\n\t\tWelcome")
    print("\t1. Show all Guitarists")
    print("\t2. Sort by price")
    print("\t3. Sort by age")
    print("\t4. Sort by Dead or Alive")
    print("\t5. Show Only Guitarist + Band")
    print("\t6. Show Only Guitars + Price")
    print("\t7. Search by Guitarists")
    print("\t8. Search by Band")
    print("\t9. Exit")
    

    choice = input("\tEnter your Choice [1 - 9]: ")
    
    print("")

    while choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5" and choice != "6" and choice != "7" and choice != "8" and choice != "9":
        print("\n\t\t***ERROR***")
        
        choice = input("\n\tEnter your Choice [1 - 9]: ")
        

    return choice

def deadOrAlive(life_search): #Sort by Dead or Alive
    if life_search == "alive":
        aliveList = []
        
        for i in range(0, len(dOrA)):
            print(f"checking to see if {dOrA[i]}")
            if dOrA[i].lower() == life_search:
                print(f"alive!")
                aliveList.append(i)
                
        return aliveList
    
    elif life_search == "dead":
        deadList = []
        
        for i in range(0, len(dOrA)):

            if dOrA[i].lower() == life_search:

                deadList.append(i)
        
        return deadList
    
def seq_search(name_search): #Search by name func

    found_index = ""

    for i in range(0, len(name)):

        if name[i] == name_search:

            found_index = i

    return found_index

def b_search(band_search): #Search by band func

    if band_search != 1:
        bandList = []

        for i in range(0, len(band)):

            if band[i] == band_search:

                bandList.append(i)
        
        return bandList
    
    else:
        found_index = ""

        for i in range(0, len(band)):

            if band[i] == b_search:

                found_index = i

        return found_index

def swap(listName, k): #Swap func
    #posi --> current position (index) of where swap needs to occur
    temp = listName[k]
    listName[k] = listName[k + 1]
    listName[k + 1] = temp

#-----loop-----------------------------------------


with open("final/finalList.txt") as csvfile: #Append loop

    file = csv.reader(csvfile)

    for rec in file:

        if len(rec) != 6:
            name.append(rec[0])
            age.append(int(rec[1]))
            dOrA.append(rec[2])
            band.append("   ")
            guitar.append(rec[3])
            price.append(int(rec[4]))
        
        else:
            name.append(rec[0])
            age.append(int(rec[1]))
            dOrA.append(rec[2])
            band.append(rec[3])
            guitar.append(rec[4])
            price.append(int(rec[5]))

        #print(rec)

os.system('cls') #clear screen function call
sleep(0.1)
menu_choice = menu()

while menu_choice != "9":
    
    if menu_choice == "1": #Showing all records
        print()
        print(f"{'NAME':18} \t {'AGE'} \t {'D-Or-A':8} \t {'BAND':23} \t {'GUITAR':30} \t {'PRICE':9}")
        print("-------------------------------------------------------------------------------------------------------------------------------------")
        for i in range(0, len(name)):
            print(f"{name[i]:15} \t {age[i]} \t {dOrA[i]:8} \t {band[i]:23} \t {guitar[i]:30} \t ${price[i]:9.2f}")

        print("-------------------------------------------------------------------------------------------------------------------------------------\n")
        input("\n\t \t \t \tPress ENTER to continue...")
        os.system('cls')
        sleep(0.1)
        menu_choice = menu()

    if menu_choice == "2": #Sort by price

        inOrDe = input("\n\tWould you like to filter PRICE in increasing or decreasing order?: ").lower()
        os.system('cls')
        sleep(0.1)
        if inOrDe == "increasing":
            for i in range(0, len(price) - 1):
                for k in range(0, len(price) - 1):
                    if price[k] > price[k + 1]:

                        swap(name, k)
                        swap(age, k)
                        swap(dOrA, k)
                        swap(band, k)
                        swap(guitar, k)
                        swap(price, k)
            print()
            print()
            print(f"{'NAME':18} \t {'AGE'} \t {'D-Or-A':8} \t {'BAND':23} \t {'GUITAR':30} \t {'PRICE':9}")
            print("-------------------------------------------------------------------------------------------------------------------------------------")
            for i in range(0, len(name)):
                print(f"{name[i]:15} \t {age[i]} \t {dOrA[i]:8} \t {band[i]:23} \t {guitar[i]:30} \t ${price[i]:9.2f}")

            print("-------------------------------------------------------------------------------------------------------------------------------------\n")
            input("\n\t \t \t \tPress ENTER to continue...")
            os.system('cls')
            sleep(0.1)
            menu_choice = menu()            

        elif inOrDe == "decreasing":
                        for i in range(0, len(age) - 1):
                            for k in range(0, len(age) - 1):
                                if price[k] < price[k + 1]:

                                    swap(name, k)
                                    swap(age, k)
                                    swap(dOrA, k)
                                    swap(band, k)
                                    swap(guitar, k)
                                    swap(price, k)

                        print()
                        print()
                        print(f"{'NAME':18} \t {'AGE'} \t {'D-Or-A':8} \t {'BAND':23} \t {'GUITAR':30} \t {'PRICE':9}")
                        print("-------------------------------------------------------------------------------------------------------------------------------------")
                        for i in range(0, len(name)):
                            print(f"{name[i]:15} \t {age[i]} \t {dOrA[i]:8} \t {band[i]:23} \t {guitar[i]:30} \t ${price[i]:9.2f}")

                        print("-------------------------------------------------------------------------------------------------------------------------------------\n")
                        input("\n\t \t \t \tPress ENTER to continue...")
                        os.system('cls')
                        sleep(0.1)
                        menu_choice = menu()
        
        else:
            print("\n\t\tChoice must be Increasing or Decreasing!!")
            input("\n\t\tPress ENTER to continue...")
            os.system('cls')
            sleep(0.1)

    if menu_choice == "3": #Sort by age
        inOrDe = input("\n\tWould you like to filter AGE in increasing or decreasing order?: ").lower()
        os.system('cls')
        sleep(0.1)
        if inOrDe == "increasing":
            for i in range(0, len(age) - 1):
                    for k in range(0, len(age) - 1):
                        if age[k] > age[k + 1]:

                            swap(name, k)
                            swap(age, k)
                            swap(dOrA, k)
                            swap(band, k)
                            swap(guitar, k)
                            swap(price, k)
            print()
            print()
            print(f"{'NAME':18} \t {'AGE'} \t {'D-Or-A':8} \t {'BAND':23} \t {'GUITAR':30} \t {'PRICE'}")
            print("-------------------------------------------------------------------------------------------------------------------------------------")
            for i in range(0, len(age)):
                print(f"{name[i]:15} \t {age[i]} \t {dOrA[i]:8} \t {band[i]:23} \t {guitar[i]:30} \t $ {price[i]}")

            print("-------------------------------------------------------------------------------------------------------------------------------------\n")
            input("\n\t \t \t \tPress ENTER to continue...")
            os.system('cls')
            sleep(0.1)
            menu_choice = menu()      

        if inOrDe == "decreasing":
            for i in range(0, len(age) - 1):
                    for k in range(0, len(age) - 1):
                        if age[k] < age[k + 1]:

                            swap(name, k)
                            swap(age, k)
                            swap(dOrA, k)
                            swap(band, k)
                            swap(guitar, k)
                            swap(price, k)

            print()
            print()
            print(f"{'NAME':18} \t {'AGE'} \t {'D-Or-A':8} \t {'BAND':23} \t {'GUITAR':30} \t {'PRICE'}")
            print("-------------------------------------------------------------------------------------------------------------------------------------")
            for i in range(0, len(age)):
                print(f"{name[i]:15} \t {age[i]} \t {dOrA[i]:8} \t {band[i]:23} \t {guitar[i]:30} \t $ {price[i]}")

            print("-------------------------------------------------------------------------------------------------------------------------------------\n")
            input("\n\t \t \t \tPress ENTER to continue...")
            os.system('cls')
            sleep(0.1)
            menu_choice = menu()    

        else:
            print("\n\t\tChoice must be Increasing or Decreasing!!")
            input("\n\t\tPress ENTER to continue...")
            os.system('cls')
            sleep(0.1)  

    if menu_choice == "4": #Sort by Dead or Alive

        search = input("\nWould you like to sort by Dead or Alive?: ").lower()
        os.system('cls')
        sleep(0.1)
        found = deadOrAlive(search)
        
        if found != "":
            print()
            print()
            print(f"{'NAME':18} \t {'AGE'} \t {'D-Or-A':8} \t {'BAND':23} \t {'GUITAR':30} \t {'PRICE':9}")
            print("-------------------------------------------------------------------------------------------------------------------------------------")
            for i in found:
                print(f"{name[i]:15} \t {age[i]} \t {dOrA[i]:8} \t {band[i]:23} \t {guitar[i]:30} \t ${price[i]:9.2f}")
            print("-------------------------------------------------------------------------------------------------------------------------------------\n")
        input("\n\t \t \t \tPress ENTER to continue...")
        os.system('cls')
        sleep(0.1)
        menu_choice = menu()            

    if menu_choice == "5": #Showing Guitarist, Age, and Band
        print()
        print()
        print(f"{'NAME':19}  {'AGE'} \t {'D-Or-A':8} \t {'BAND':24}")
        print("---------------------------------------------------------------")
        for i in range(0, len(name)):
            print(f"{name[i]:20} {age[i]} \t {dOrA[i]:8} \t {band[i]:25}")

        print("---------------------------------------------------------------\n")
        input("\n\t \t \t \tPress ENTER to continue...")
        os.system('cls')
        sleep(0.1)
        menu_choice = menu()

    if menu_choice == "6": #Showing Guitar + Price
        print()
        print()
        print(f"{'GUITAR':35} \t {'PRICE':9}")
        print("------------------------------------------------------")
        for i in range(0, len(name)):
            print(f"{guitar[i]:35} \t ${price[i]:9.2f}")

        print("------------------------------------------------------\n")
        input("\n\t \t \t \tPress ENTER to continue...")
        os.system('cls')
        sleep(0.1)
        menu_choice = menu()
        
    if menu_choice == "7": #Search by Name
        search = input("\nEnter the NAME of the guitarist you are searching for: ")
        os.system('cls')
        sleep(0.1)
        found = seq_search(search)

        if found != "":
            print()
            print()
            print(f"{'NAME':18} \t {'AGE'} \t {'D-Or-A':8} \t {'BAND':23} \t {'GUITAR':30} \t {'PRICE':9}")
            print("-------------------------------------------------------------------------------------------------------------------------------------")
            print(f"{name[found]:15} \t {age[found]} \t {dOrA[found]:8} \t {band[found]:23} \t {guitar[found]:30} \t ${price[found]:9.2f}")
            print("-------------------------------------------------------------------------------------------------------------------------------------\n")

        else:
            print(f"Could not find {search} in the list, either you misspelled the name or they are not in the list yet.")
        
        input("\n\t \t \t \tPress ENTER to continue...")
        os.system('cls')
        sleep(0.1)
        menu_choice = menu()

    if menu_choice == "8": #Search by Band
        search = input("\nEnter the BAND of the guitarist(s) you are searching for: ")
        os.system('cls')
        sleep(0.1)
        found = b_search(search)

        if found != "":
            print()
            print()
            print(f"{'NAME':18} \t {'AGE'} \t {'D-Or-A':8} \t {'BAND':23} \t {'GUITAR':30} \t {'PRICE':9}")
            print("-------------------------------------------------------------------------------------------------------------------------------------")
            for i in found:
                print(f"{name[i]:15} \t {age[i]} \t {dOrA[i]:8} \t {band[i]:23} \t {guitar[i]:30} \t ${price[i]:9.2f}")
            print("-------------------------------------------------------------------------------------------------------------------------------------\n")

        else:
            print(f"Could not find {search} in the list, either you misspelled the name or that band is not in the list yet.")

        input("\n\t \t \t \tPress ENTER to continue...")
        os.system('cls')
        sleep(0.1)
        menu_choice = menu()


os.system('cls')
sleep(0.1)
print("\n\n\t\tThank you for using this program. Have a nice day and Rock on!\n\n")




