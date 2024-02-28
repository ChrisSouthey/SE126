import csv
from os import system, name
from time import sleep

#Creating empty lists
rowNum = []
seatA = []
seatB = []
seatC = []
seatD = []
selectionList = []


with open("week8/hw/airconditioning.txt") as csvfile:
    file = csv.reader(csvfile)
    for rec in file:


        rowNum.append(rec[0])
        seatA.append(rec[1])
        seatB.append(rec[2])
        seatC.append(rec[3])
        seatD.append(rec[4])


#---FUNCTIONS------------------------------------
#Clear function
def clear():  

     # for windows  
     if name == 'nt':
          _ = system('cls')  
     # for mac and linux(here, os.name is 'posix')  
     else:  
          _ = system('clear') 

#Funtion to show seating chart    
def chart():


    if answer == "y":
        print()
        print("------------------------------")
        print("| Row #     -  -       -  -  |")
        for i in range(0, len(rowNum)):
            print(f"| Row {rowNum[i]}     {seatA[i]}  {seatB[i]}       {seatC[i]}  {seatD[i]}  |")
        print("------------------------------")

#Getting the row #
def get_row():

    row_r = -1

    while row_r < 1 or row_r > 7:

        try:
            row_r = int(input("Enter the ROW you want to sit in [1-7]: "))

        except:
            print("Must be a number between 1 and 7!!!")
    return row_r
    
#Getting the Seat letter
def get_seat():

    acceptable_seats = ["A", "B", "C", "D"]

    seat_r = input("Enter the SEAT you wish to sit in [A-D]: ").upper()


    while seat_r not in acceptable_seats:
        print("Seat must be either A, B, C, or D!!!")
        seat_r = input("Enter the SEAT you wish to sit in [A-D]: ").upper()

    return seat_r

answer = "y"
clear()
answer = input("\nWould you like to reserve a seat? [Y or N]: ").lower()

while answer == "y":
    
    chart()

    row_req = get_row()
    seat_req = get_seat()

    seatSel = str(row_req) + seat_req

    
    

    print(f"\nYou have chosen seat {seatSel}")

    #Replacing selected seat with an X
    if seat_req == "A":

        if seatA[row_req - 1] != "X":
            print("\nThis seat is available!")
            seatA[row_req - 1] = "X"

        else:
            print(f"\n\nSorry, the seat {row_req}{seat_req} is taken.")
            
    

    elif seat_req == "B":

        if seatB[row_req - 1] != "X":
            print("\nThis seat is available!")
            seatB[row_req - 1] = "X"

        else:
            print(f"\n\nSorry, the seat {row_req}{seat_req} is taken.")
            
    

    elif seat_req == "C":

        if seatC[row_req - 1] != "X":
            print("\nThis seat is available!")
            seatC[row_req - 1] = "X"

        else:
            print(f"\n\nSorry, the seat {row_req}{seat_req} is taken.")
            
    

    elif seat_req == "D":

        if seatD[row_req - 1] != "X":
            print("\nThis seat is available!")
            seatD[row_req - 1] = "X"

        else:
            print(f"\n\nSorry, the seat {row_req}{seat_req} is taken.")

            
    answer = input("\nEnter Y to confirm selection or C to cancel: ").lower()

    if answer == "y":
        selectionList.append(seatSel)
        clear()
        sleep(0.1)
        chart()
    
    elif answer == "c":
        clear()
        print("\nSeat selection canceled")


    print(f"\nSeats chosen: {selectionList}")
    answer = input("\nWould you like to select another seat? [y/n]: ").lower()
    
    if answer == "y":
        clear()
        sleep(0.1)

    else:
        clear()
        sleep(0.1)


chart()
print(f"\nYou have chosen seats {selectionList}")

print("\nThank you for flying with us! Please enjoy your Travels.")

