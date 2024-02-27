import csv

#Creating empty lists
rowNum = []
seatA = []
seatB = []
seatC = []
seatD = []


with open("week8/hw/airconditioning.txt") as csvfile:
    file = csv.reader(csvfile)
    for rec in file:


        rowNum.append(rec[0])
        seatA.append(rec[1])
        seatB.append(rec[2])
        seatC.append(rec[3])
        seatD.append(rec[4])



#Funtion to select seat    
def chart():

    answer = input("\nWould you like to reserve a seat? [Y or N]: ").lower()

    if answer == "y":
        print()
        print("------------------------------")
        print("| Row #     -  -       -  -  |")
        for i in range(0, len(rowNum)):
            print(f"| Row {rowNum[i]}     {seatA[i]}  {seatB[i]}       {seatC[i]}  {seatD[i]}  |")
        print("------------------------------")


def get_row():

    row_r = -1

    while row_r < 1 or row_r > 7:

        try:
            row_r = int(input("Enter the ROW you want to sit in [1-7]: "))

        except:
            print("Must be a number between 1 and 7!!!")
    return row_r
    

def get_seat():

    acceptable_seats = ["A", "B", "C", "D"]

    seat_r = input("Enter the SEAT you wish to sit in [A-D]: ").upper()


    while seat_r not in acceptable_seats:
        print("Seat must be either A, B, C, or D!!!")
        seat_r = input("Enter the SEAT you wish to sit in [A-D]: ").upper()

    return seat_r

answer = "y"

while answer == "y":
    chart()

    row_req = get_row()
    seat_req = get_seat()


    print(f"\nYou have chosen seat {row_req}{seat_req}")

    if seat_req == "A":

        if seatA[row_req - 1] != "X":
            print("This seat is available!")
            seatA[row_req - 1] = "X"

        else:
            print(f"\n\nSorry, the seat {row_req}{seat_req} is taken.")
            
    answer = input("Would you liek to select another seat? [y/n]: ")

    if seat_req == "B":

        if seatA[row_req - 1] != "X":
            print("This seat is available!")
            seatA[row_req - 1] = "X"

        else:
            print(f"\n\nSorry, the seat {row_req}{seat_req} is taken.")
            
    answer = input("Would you liek to select another seat? [y/n]: ")

    if seat_req == "C":

        if seatA[row_req - 1] != "X":
            print("This seat is available!")
            seatA[row_req - 1] = "X"

        else:
            print(f"\n\nSorry, the seat {row_req}{seat_req} is taken.")
            
    answer = input("Would you liek to select another seat? [y/n]: ")

    if seat_req == "D":

        if seatA[row_req - 1] != "X":
            print("This seat is available!")
            seatA[row_req - 1] = "X"

        else:
            print(f"\n\nSorry, the seat {row_req}{seat_req} is taken.")
            
    answer = input("Would you liek to select another seat? [y/n]: ")
    


