import csv
from os import system, name
from time import sleep
import random

#Chris Southey
#SE126 Intermidiate prog using Python
#Final Lab

#03-06-24

#Write a program that can be used by a small theater to sell tickets for performances. The theater’s auditorium has 15 rows of seats with 30 seats in each row. The program should display a screen that shows which seats are available and which are taken. Seats thar are available are represented by # and seats that are taken are represent by a *. There are aisles after seats H and V.

#-----Lists----------------------------------------------------------
rowNum = []  #Lotta lists 0_0
row1 = []
row2 = []
row3 = []
row4 = []
row5 = []
row6 = []
row7 = []
row8 = []
isle1 = []
row9 = []
row10 = []
row11 = []
row12 = []
row13 = []
row14 = []
row15 = []
row16 = []
row17 = []
row18 = []
row19 = []
row20 = []
row21 = []
row22 = []
row23 = []
isle2 = []
row24 = []
row25 = []
row26 = []
row27 = []
row28 = []
row29 = []
row30 = []
seatList = []
rowList = []



#-----Functions------------------------------------------------------
#Clear function
def clear():  

     # for windows  
     if name == 'nt':
          _ = system('cls')  
     # for mac and linux(here, os.name is 'posix')  
     else:  
          _ = system('clear') 

#Seating Chart function
def seatingChart():
     
     if answer == "y":
        print("-------------------------------------------------------------------------")
        print("| Row  \t\t\t\t   Seats \t\t\t\t|")
        print("| \tA B C D E F G H   I J K L M N O P Q R S T U V   W X Y Z 1 2 3 4 |")
        for i in range(0, len(rowNum)):
               print(f"| {rowNum[i]}\t{row1[i]} {row2[i]} {row3[i]} {row4[i]} {row5[i]} {row6[i]} {row7[i]} {row8[i]} {isle1[i]} {row9[i]} {row10[i]} {row11[i]} {row12[i]} {row13[i]} {row14[i]} {row15[i]} {row16[i]} {row17[i]} {row18[i]} {row19[i]} {row20[i]} {row21[i]} {row22[i]} {row23[i]} {isle2[i]} {row24[i]} {row25[i]} {row26[i]} {row27[i]} {row28[i]} {row29[i]} {row30[i]} |")
        print("-------------------------------------------------------------------------")
          
def getRow():
     
    row_r = -1

    while row_r < 1 or row_r > 15:
         
            try:
                 row_r = int(input("\n\tEnter the ROW you wish to sit in [1 - 15]: "))

            except:
                 print("\t\nThe row must be between 1 and 15!!!")

            return row_r

def getSeat():
     
        seats = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", ]

        seat_r = input("\n\tEnter the SEAT you wish to sit in [A - Z or 1 - 4]: ").upper()

        while seat_r not in seats:
          print("The seat must be A - Z or 1 - 4!!!")
          seat_r = input("Enter the SEAT you wish to sit in [A - Z or 1 - 4]: ").upper()

        return seat_r

def goodbye():
    print("\t\tSeats Reserved")
    print("\t----------------------------")
    print("\t| Row# \t Seat\t\t   |")
    for i in range(0, len(seatList)):
        print(f"\t| {rowList[i]} \t {seatList[i]} \t\t   |")
    print("\t----------------------------")
    print("\n\t\tEnjoy your movie!\n")
#-----Main Code------------------------------------------------------
with open("week9/hw/finalLab.txt") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:

        rowNum.append(rec[0])
        row1.append(rec[1])
        row2.append(rec[2])
        row3.append(rec[3])
        row4.append(rec[4])
        row5.append(rec[5])
        row6.append(rec[6])
        row7.append(rec[7])
        row8.append(rec[8])
        isle1.append(rec[9])
        row9.append(rec[10])
        row10.append(rec[11])
        row11.append(rec[12])
        row12.append(rec[13])
        row13.append(rec[14])
        row14.append(rec[15])
        row15.append(rec[16])
        row16.append(rec[17])
        row17.append(rec[18])
        row18.append(rec[19])
        row19.append(rec[20])
        row20.append(rec[21])
        row21.append(rec[22])
        row22.append(rec[23])
        row23.append(rec[24])
        isle2.append(rec[25])
        row24.append(rec[26])
        row25.append(rec[27])
        row26.append(rec[28])
        row27.append(rec[29])
        row28.append(rec[30])
        row29.append(rec[31])
        row30.append(rec[32])


answer = "y"
movieList = ["Kung Fu Panda 4", "Dune: Part Two", "Madame Web", "Migration", "Imaginary", "Wonka", "Oppenheimer", "Trolls Band Together", "Wish"] #Fun little code to make it show different movies when you select seats :)

clear()
answer = input(f"\n\n\tWould you like to reserve a seat for {random.choice(movieList)} [y/n]?: ").lower()
sleep(0.1)

while answer == "y":
    clear()
    seatingChart()

    rowReq = getRow()
    seatReq = getSeat()

    #AHHHHHHHHHHHHHHHHHHHHHHHHHH
    #I probably did this the hard way
    
    if seatReq == "A":
        if row1[rowReq - 1] != "*":
            print("\n\tThis seat is availible!")
            row1[rowReq - 1] = "*"

        else:
            print(f"\n\tSorry, seat {seatReq} in row {rowReq} is not availible ")

    if seatReq == "B":
        if row2[rowReq - 1] != "*":
            print("\n\tThis seat is availible!")
            row2[rowReq - 1] = "*"

        else:
            print(f"\n\tSorry, seat {seatReq} in row {rowReq} is not availible ")

    if seatReq == "C":
        if row3[rowReq - 1] != "*":
            print("\n\tThis seat is availible!")
            row3[rowReq - 1] = "*"

        else:
            print(f"\n\tSorry, seat {seatReq} in row {rowReq} is not availible ")

    if seatReq == "D":
        if row4[rowReq - 1] != "*":
            print("\n\tThis seat is availible!")
            row4[rowReq - 1] = "*"

        else:
            print(f"\n\tSorry, seat {seatReq} in row {rowReq} is not availible ")

    if seatReq == "E":
        if row5[rowReq - 1] != "*":
            print("\n\tThis seat is availible!")
            row5[rowReq - 1] = "*"

        else:
            print(f"\n\tSorry, seat {seatReq} in row {rowReq} is not availible ")

    if seatReq == "F":
        if row6[rowReq - 1] != "*":
            print("\n\tThis seat is availible!")
            row6[rowReq - 1] = "*"

        else:
            print(f"\n\tSorry, seat {seatReq} in row {rowReq} is not availible ")

    if seatReq == "G":
        if row7[rowReq - 1] != "*":
            print("\n\tThis seat is availible!")
            row7[rowReq - 1] = "*"

        else:
            print(f"\n\tSorry, seat {seatReq} in row {rowReq} is not availible ")

    if seatReq == "H":
        if row8[rowReq - 1] != "*":
            print("\n\tThis seat is availible!")
            row8[rowReq - 1] = "*"

        else:
            print(f"\n\tSorry, seat {seatReq} in row {rowReq} is not availible ")

    if seatReq == "I":
        if row9[rowReq - 1] != "*":
            print("\n\tThis seat is availible!")
            row9[rowReq - 1] = "*"

        else:
            print(f"\n\tSorry, seat {seatReq} in row {rowReq} is not availible ")

    if seatReq == "J":
        if row10[rowReq - 1] != "*":
            print("\n\tThis seat is availible!")
            row10[rowReq - 1] = "*"

        else:
            print(f"\n\tSorry, seat {seatReq} in row {rowReq} is not availible ")

    if seatReq == "K":
            if row11[rowReq - 1] != "*":
                print("\n\tThis seat is availible!")
                row11[rowReq - 1] = "*"

            else:
                print(f"\n\tSorry, seat {seatReq} in row {rowReq} is not availible ")

    if seatReq == "L":
        if row12[rowReq - 1] != "*":
            print("\n\tThis seat is availible!")
            row12[rowReq - 1] = "*"

        else:
            print(f"\n\tSorry, seat {seatReq} in row {rowReq} is not availible ")

    if seatReq == "M":
        if row13[rowReq - 1] != "*":
            print("\n\tThis seat is availible!")
            row13[rowReq - 1] = "*"

        else:
            print(f"\n\tSorry, seat {seatReq} in row {rowReq} is not availible ")

    if seatReq == "N":
        if row14[rowReq - 1] != "*":
            print("\n\tThis seat is availible!")
            row14[rowReq - 1] = "*"

        else:
            print(f"\n\tSorry, seat {seatReq} in row {rowReq} is not availible ")

    if seatReq == "O":
        if row15[rowReq - 1] != "*":
            print("\n\tThis seat is availible!")
            row15[rowReq - 1] = "*"

        else:
            print(f"\n\tSorry, seat {seatReq} in row {rowReq} is not availible ")

    if seatReq == "P":
        if row16[rowReq - 1] != "*":
            print("\n\tThis seat is availible!")
            row16[rowReq - 1] = "*"

        else:
            print(f"\n\tSorry, seat {seatReq} in row {rowReq} is not availible ")

    if seatReq == "Q":
        if row17[rowReq - 1] != "*":
            print("\n\tThis seat is availible!")
            row17[rowReq - 1] = "*"

        else:
            print(f"\n\tSorry, seat {seatReq} in row {rowReq} is not availible ")

    if seatReq == "R":
        if row18[rowReq - 1] != "*":
            print("\n\tThis seat is availible!")
            row18[rowReq - 1] = "*"

        else:
            print(f"\n\tSorry, seat {seatReq} in row {rowReq} is not availible ")

    if seatReq == "S":
        if row19[rowReq - 1] != "*":
            print("\n\tThis seat is availible!")
            row19[rowReq - 1] = "*"

        else:
            print(f"\n\tSorry, seat {seatReq} in row {rowReq} is not availible ")

    if seatReq == "T":
        if row20[rowReq - 1] != "*":
            print("\n\tThis seat is availible!")
            row20[rowReq - 1] = "*"

        else:
            print(f"\n\tSorry, seat {seatReq} in row {rowReq} is not availible ")

    if seatReq == "U":
        if row21[rowReq - 1] != "*":
            print("\n\tThis seat is availible!")
            row21[rowReq - 1] = "*"

        else:
            print(f"\n\tSorry, seat {seatReq} in row {rowReq} is not availible ")

    if seatReq == "V":
        if row22[rowReq - 1] != "*":
            print("\n\tThis seat is availible!")
            row22[rowReq - 1] = "*"

        else:
            print(f"\n\tSorry, seat {seatReq} in row {rowReq} is not availible ")

    if seatReq == "W":
        if row23[rowReq - 1] != "*":
            print("\n\tThis seat is availible!")
            row23[rowReq - 1] = "*"

        else:
            print(f"\n\tSorry, seat {seatReq} in row {rowReq} is not availible ")

    if seatReq == "X":
        if row24[rowReq - 1] != "*":
            print("\n\tThis seat is availible!")
            row24[rowReq - 1] = "*"

        else:
            print(f"\n\tSorry, seat {seatReq} in row {rowReq} is not availible ")

    if seatReq == "Y":
            if row25[rowReq - 1] != "*":
                print("\n\tThis seat is availible!")
                row25[rowReq - 1] = "*"

            else:
                print(f"\n\tSorry, seat {seatReq} in row {rowReq} is not availible ")

    if seatReq == "Z":
        if row26[rowReq - 1] != "*":
            print("\n\tThis seat is availible!")
            row26[rowReq - 1] = "*"

        else:
            print(f"\n\tSorry, seat {seatReq} in row {rowReq} is not availible ")

    if seatReq == "1":
        if row27[rowReq - 1] != "*":
            print("\n\tThis seat is availible!")
            row27[rowReq - 1] = "*"

        else:
            print(f"\n\tSorry, seat {seatReq} in row {rowReq} is not availible ")

    if seatReq == "2":
            if row28[rowReq - 1] != "*":
                print("\n\tThis seat is availible!")
                row28[rowReq - 1] = "*"

            else:
                print(f"\n\tSorry, seat {seatReq} in row {rowReq} is not availible ")

    if seatReq == "3":
        if row29[rowReq - 1] != "*":
            print("\n\tThis seat is availible!")
            row29[rowReq - 1] = "*"

        else:
            print(f"\n\tSorry, seat {seatReq} in row {rowReq} is not availible ")

    if seatReq == "4":
        if row30[rowReq - 1] != "*":
            print("\n\tThis seat is availible!")
            row30[rowReq - 1] = "*"

        else:
            print(f"\n\tSorry, seat {seatReq} in row {rowReq} is not availible ")


    answer = input("\n\tWould you like to reserve this seat? [y/n]: ").lower()

    if answer == "y":
         seatList.append(seatReq)
         rowList.append(rowReq)
         clear()
         seatingChart()
         print("\n\tYou have reserved this seat!")

    answer = input("\n\tWould you like to reserve another seat? [y/n]: ")

    if answer == "y":
        clear()
        

    else:
        clear()
        
goodbye()
