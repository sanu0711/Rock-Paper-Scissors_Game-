import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]
print("----------------------------------------------------------------------")
print("\t\t! WELCOME TO ROCK PAPER SCISSORS GAME !")
print("----------------------------------------------------------------------")
print("What do you choose?\n0 for Rock\n1 for Paper\n2 for Scissors.\n")

user_choice = int(input("Enter your choice : "))
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you Lose!")
else:
    print(game_images[user_choice])

    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer_choice])

    print("----------------------------------------------------------------------")


    if user_choice == 0 and computer_choice == 2:
        print("You Win!".center(70))
    elif computer_choice == 0 and user_choice == 2:
        print("You Lose".center(70))
    elif computer_choice > user_choice:
        print("You Lose".center(70))
    elif user_choice > computer_choice:
        print("You Win!".center(70))
    elif computer_choice == user_choice:
        print("It's a Draw".center(70))

    print("----------------------------------------------------------------------")