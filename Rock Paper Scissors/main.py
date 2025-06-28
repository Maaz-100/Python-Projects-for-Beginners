import random

while True:
    restart = input("Would you like to restart y/n ")
    if restart == "y" or restart == "Y":
        print("")
        user_choice = input("chose either r/p/s ")
        computer_choice = random.randint(1, 3)

        if computer_choice == 1:
            computer_choice = "rock"

        elif computer_choice == 2:
            computer_choice = "paper"

        elif computer_choice == 3:
            computer_choice = "scissor"

        print("computer chose ", computer_choice)

        if user_choice == "r" and computer_choice == "paper":
            print("You Loose ")

        elif user_choice == "r" and computer_choice == "scissor":
            print("You win ")

        elif user_choice == "r" and computer_choice == "rock":
            print("You have drawn ")



        elif user_choice == "p" and computer_choice == "paper":
            print("You have drawn ")

        elif user_choice == "p" and computer_choice == "scissor":
            print("You Loose ")

        elif user_choice == "p" and computer_choice == "rock":
            print("You Won ")



        elif user_choice == "s" and computer_choice == "scissor":
            print("You Drawn ")

        elif user_choice == "s" and computer_choice == "paper":
            print("You Win ")

        elif user_choice == "s" and computer_choice == "Rock":
            print("You Loose ")



    elif restart == "n" or restart == "N":
        print("")
        break

    else:
        print("")
        print("Type y or no")