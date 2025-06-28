import random
while True:
    roll = input("Roll dice? y/n ")

    if roll == "n" or roll == "N" :
        break

    elif roll == "y" or roll == "Y" :
        print("Dice 1:",random.randint(1, 6))
        print("Dice 2:",random.randint(1, 6))

    else:
        print("chose either y or n")
