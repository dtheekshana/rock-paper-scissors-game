# import the random module
import random
while(True): # creating a loop because user can play this game as his or her wish times
  print("Dear user you have option!, they are:")
  print("'rock','paper','scissors'")
  # take input from the user using input() function in python.
  # Then create the computer choice using randint() function from the Random module.
  userchoice = input("Enter your choice: ")
  com_choice = random.randint(1,3)
  # Now, we will convert the computer's input from 1, 2, 3 into 'p', 'r','s'.
  if com_choice == 1:
    com_choice = "rock"
  elif com_choice == 2:
    com_choice = "paper"
  elif com_choice == 3:
    com_choice = "scissors"
  else:
    print("sorry, something went wrong!")
# Now, compare the user choice with computer choice using nested if...else.
# And if both choices are same there is a tie.
  if com_choice == userchoice:
    print("It's a tie")
  elif userchoice == "rock":
    if com_choice == "scissors":
      print("Congratulations,you won !")
    else:
      print("Computer won!")
  elif userchoice == "paper":
    if com_choice == "rock":
      print("Congratulations,you won !")
    else:
      print("Computer won!")
  elif userchoice == "scissors":
    if com_choice == "paper":
      print("Congratulation,you won !")
    else:
      print("Computer won")
    # Now, take input whether the user wants to play again if no then break the loop.
  print("Do you want to play agin?")
  print("Then Enter (y/n) for answer")
  ans = input()
  if ans == "n" or ans == "N":
    break