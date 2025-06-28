import random

count = 0
B_Score = 500

while True:
    carry_on = input("Do you wish to restart: Y/N ")
    if carry_on == "Y" or carry_on == "y":
        random_max = int(input("What's the max number that you would like to guess to "))
        random_min = int(input("What's the min number that you would like to guess to "))
        to_guess = random.randint(random_min, random_max)

        while True:
            guess = int(input("Guess a number: "))
            if guess != to_guess:
                count += 1
                print("Wrong number")
                print("Attempts:", count)

                if guess < to_guess:
                    print("Try higher")
                else:
                    print("Try lower")
                print("")

            else:
                print("It took you", count, "guesses to guess the number")

                if count < B_Score:
                    print("You beat the best score of", B_Score)
                    B_Score = count
                elif count > B_Score:
                    print("You didn't beat the best score of", B_Score)
                else:
                    print("You got the same as the best score. The best score will not change")

                count = 0
                break

    elif carry_on.lower() == "n":
        break

    else:
        print("You have to input Y or N")

print("The best score was", B_Score)
