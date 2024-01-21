def difference(people, max_cap):
  if people > max_cap:
      over = int(people - max_cap)
      print(f"\t\t\n\nYou must remove {over} people from the meeting to meet the fire safety requirments!")
  elif people < max_cap:
    extra = int(max_cap - people)
    print(f"\t\t\n\nYou can still fit {extra} people into the meeting!")
  
def decision():

  responce = input("\n\nWould you like to enter another meeting? [y/n]: ").lower()
  
  while responce != "y" and responce != "n":
    print("\t\t\n\n***INVALID ENTRY***")
    responce = input("\n\nWould you like to enter another meeting? [y/n]: ").lower()
    
  return responce
#---------------------------------------
answer = "y"

print("Welcome to the fire safety program")
while answer == "y":

  name = input("\n\nWhat is the name for the group meeting?: ")
  
  attend = float(input("\nHow many people are attendng the meeting?: "))

  cap = float(input("\nWhat is the max compacity of the meeting room?: "))
  
  difference(attend, cap)

  answer = decision()



print("\n\nThank you for using this program, Have a nice meeting.")
