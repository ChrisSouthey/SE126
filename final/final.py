import csv
import os
from os import system, name
from time import sleep

#Chris Southey
#Midterm project
#The user will see a printed list of famous guitarists, the band they are in, Their signature guitar, and the average price of that guitar, and be able to search for a specific guitarist

#-----Lists-----------------------------------------
name = []
age = []
dOrA = []
band = []
guitar = []
price = []




#-----Functions-------------------------------------
def clear(): #Clear func

     # for windows  
     if name == 'nt':
          _ = os.system('cls')  
     # for mac and linux(here, os.name is 'posix')  
     else:  
          _ = system('clear') 



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

            if dOrA[i] == "alive":
                
                aliveList.append(i)
                
        return aliveList
    
    elif life_search == "dead":
        deadList = []
        
        for i in range(0, len(dOrA)):

            if dOrA[i] == "dead":

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

def swap(price, k): #Swap func
    #posi --> current position (index) of where swap needs to occur
    temp = price[k]
    price[k] = price[k + 1]
    price[k + 1] = temp

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

menu_choice = menu()



while menu_choice != "9":
    
    if menu_choice == "1": #Showing all records
        print()
        print(f"{'NAME':18} \t {'AGE'} \t {'D-Or-A':8} \t {'BAND':23} \t {'GUITAR':30} \t {'PRICE':9}")
        print("-------------------------------------------------------------------------------------------------------------------------------------")
        for i in range(0, len(name)):
            print(f"{name[i]:15} \t {age[i]} \t {dOrA[i]:8} \t {band[i]:23} \t {guitar[i]:30} \t ${price[i]:9.2f}")

        print("-------------------------------------------------------------------------------------------------------------------------------------\n")
        menu_choice = menu()

    if menu_choice == "2": #Sort by price

        inOrDe = input("\n\tWould you like to filter in increasing or decreasing order?: ").lower()

        if inOrDe == "increasing":
            for i in range(0, len(price) - 1):
                for k in range(0, len(price) - 1):
                    if price[k] > price[k + 1]:

                        #swap values
                        ageSwap = price[k]
                        price[k] = price[k + 1]
                        price[k + 1] = ageSwap

                        swap(name, k)
                        swap(age, k)
                        swap(dOrA, k)
                        swap(band, k)
                        swap(guitar, k)
                        swap(price, k)

            print(f"{'NAME':18} \t {'AGE'} \t {'D-Or-A':8} \t {'BAND':23} \t {'GUITAR':30} \t {'PRICE':9}")
            print("-------------------------------------------------------------------------------------------------------------------------------------")
            for i in range(0, len(name)):
                print(f"{name[i]:15} \t {age[i]} \t {dOrA[i]:8} \t {band[i]:23} \t {guitar[i]:30} \t ${price[i]:9.2f}")

            print("-------------------------------------------------------------------------------------------------------------------------------------\n")
            menu_choice = menu()            

        elif inOrDe == "decreasing":
                        for i in range(0, len(age) - 1):
                            for k in range(0, len(age) - 1):
                                if price[k] < price[k + 1]:

                                    #swap values
                                    ageSwap = price[k]
                                    price[k] = price[k + 1]
                                    price[k + 1] = ageSwap

                                    swap(name, k)
                                    swap(age, k)
                                    swap(dOrA, k)
                                    swap(band, k)
                                    swap(guitar, k)
                                    swap(price, k)

        print(f"{'NAME':18} \t {'AGE'} \t {'D-Or-A':8} \t {'BAND':23} \t {'GUITAR':30} \t {'PRICE':9}")
        print("-------------------------------------------------------------------------------------------------------------------------------------")
        for i in range(0, len(name)):
            print(f"{name[i]:15} \t {age[i]} \t {dOrA[i]:8} \t {band[i]:23} \t {guitar[i]:30} \t ${price[i]:9.2f}")

        print("-------------------------------------------------------------------------------------------------------------------------------------\n")
        menu_choice = menu()
            
    if menu_choice == "3": #Sort by age
        for i in range(0, len(age) - 1):
                for k in range(0, len(age) - 1):
                    if age[k] > age[k + 1]:

                        #swap values
                        ageSwap = age[k]
                        age[k] = age[k + 1]
                        age[k + 1] = ageSwap

                        swap(name, k)
                        swap(age, k)
                        swap(dOrA, k)
                        swap(band, k)
                        swap(guitar, k)
                        swap(price, k)

        print(f"{'NAME':18} \t {'AGE'} \t {'D-Or-A':8} \t {'BAND':23} \t {'GUITAR':30} \t {'PRICE'}")
        print("-------------------------------------------------------------------------------------------------------------------------------------")
        for i in range(0, len(age)):
            print(f"{name[i]:15} \t {age[i]} \t {dOrA[i]:8} \t {band[i]:23} \t {guitar[i]:30} \t $ {price[i]}")

        print("-------------------------------------------------------------------------------------------------------------------------------------\n")
        menu_choice = menu()      

    if menu_choice == "4": #Sort by Dead or Alive

        search = input("\nWould you like to sort by Dead or Alive?: ").lower()

        found = deadOrAlive(search)
        
        if found != "":
            
            print(f"{'NAME':18} \t {'AGE'} \t {'D-Or-A':8} \t {'BAND':23} \t {'GUITAR':30} \t {'PRICE':9}")
            print("-------------------------------------------------------------------------------------------------------------------------------------")
            for i in found:
                print(f"{name[i]:15} \t {age[i]} \t {dOrA[i]:8} \t {band[i]:23} \t {guitar[i]:30} \t ${price[i]:9.2f}")
            print("-------------------------------------------------------------------------------------------------------------------------------------\n")

        menu_choice = menu()            

    if menu_choice == "5": #Showing Guitarist, Age, and Band
        print(f"{'NAME':19}  {'AGE'} \t {'D-Or-A':8} \t {'BAND':24}")
        print("---------------------------------------------------------------")
        for i in range(0, len(name)):
            print(f"{name[i]:20} {age[i]} \t {dOrA[i]:8} \t {band[i]:25}")

        print("---------------------------------------------------------------\n")
        menu_choice = menu()

    if menu_choice == "6": #Showing Guitar + Price
        print(f"{'GUITAR':35} \t {'PRICE':9}")
        print("------------------------------------------------------")
        for i in range(0, len(name)):
            print(f"{guitar[i]:35} \t ${price[i]:9.2f}")

        print("------------------------------------------------------\n")
        menu_choice = menu()
        
    if menu_choice == "7": #Search by Name
        search = input("\nEnter the NAME of the guitarist you are searching for: ")

        found = seq_search(search)

        if found != "":
            print(f"{'NAME':18} \t {'AGE'} \t {'D-Or-A':8} \t {'BAND':23} \t {'GUITAR':30} \t {'PRICE':9}")
            print("-------------------------------------------------------------------------------------------------------------------------------------")
            print(f"{name[found]:15} \t {age[found]} \t {dOrA[found]:8} \t {band[found]:23} \t {guitar[found]:30} \t ${price[found]:9.2f}")
            print("-------------------------------------------------------------------------------------------------------------------------------------\n")

        else:
            print(f"Could not find {search} in the list, either you misspelled the name or they are not in the list.")

        menu_choice = menu()

    if menu_choice == "8": #Search by Band
        search = input("\nEnter the BAND of the guitarist(s) you are searching for: ")

        found = b_search(search)

        if found != "":
            print(f"{'NAME':18} \t {'AGE'} \t {'D-Or-A':8} \t {'BAND':23} \t {'GUITAR':30} \t {'PRICE':9}")
            print("-------------------------------------------------------------------------------------------------------------------------------------")
            for i in found:
                print(f"{name[i]:15} \t {age[i]} \t {dOrA[i]:8} \t {band[i]:23} \t {guitar[i]:30} \t ${price[i]:9.2f}")
            print("-------------------------------------------------------------------------------------------------------------------------------------\n")

        else:
            print(f"Could not find {search} in the list, either you misspelled the name or they are not in the list.")

        menu_choice = menu()

    
print("Thank you for using this program. Have a nice day and Rock on!")





