import random
print("----------------------------")
print("The Rock Paper Scissors Game\n")
# Creating our choices list
choices = ["rock", "paper", "scissors"]
# Using while loop to keep game going
while True:
# setting random choice for computer
  random_index = random.randint(0,2)
  computer_choice = choices[random_index]

  user_choice = input("Please enter 1 for rock 2 for paper 3 for scissors \nor -1 to quit: ")
#   If user enters -1 the game quits
  if user_choice == "-1":
    print("Goodbye!")
    break
  else:
    if user_choice == "1":
        user_choice = "rock"
    if user_choice == "2":
        user_choice = "paper"
    if user_choice == "3":
        user_choice = "scissors"
    print()
    print("You chose:", user_choice)
    print("The computer chose:", computer_choice)
    print()
# Checking user input and comparing it to computer's
  if user_choice == 'rock':
    if computer_choice == 'rock':
      print("The match was a tie")
    elif computer_choice == 'scissors':
      print("Congratulations you win!")
    elif computer_choice == 'paper':
      print("Sorry you lose!")
  elif user_choice == 'paper':
    if computer_choice == 'paper':
      print("The match was a tie")
    elif computer_choice == 'rock':
      print("Congratulations you win!")
    elif computer_choice == 'scissors':
      print("Sorry you lose!")
  elif user_choice == 'scissors':
    if computer_choice == 'scissors':
      print("The match was a tie")
    elif computer_choice == 'paper':
      print("Congratulations you win!")
    elif computer_choice == 'rock':
      print("Sorry you lose!")
print("----------------------------")


 