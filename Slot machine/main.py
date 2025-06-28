import random


keys = {1: "🙂", 2: "⭐", 3: "🍒", 4: "🍌", 5: "🪙", 6: "🍋", 7: "7", 8: "🍀", 9: "💎"}

balance = int(input("enter starting amount "))


while True:

    bet = int(input("enter your betting amount "))
    if bet > balance:
        print("you dont have that much funds")
    else:

        print("bet taken")
        balance = balance - bet
        print("your balance is now ", balance)
        print("")

        x = random.randint(1, 9)
        y = random.randint(1, 9)
        z = random.randint(1, 9)

        print(f"{keys[x]} | {keys[y]} | {keys[z]}")

        if x == y == z:
            print("that was  very lucky heres your money")

            balance = (bet * 10) + balance

            print("")
            print("your balance", balance)

        elif x != y != z:
            print("sorry you loss your bet")
            print("your balance", balance)
            print("")

        else:
            print("that was lucky heres your money")

            balance = (bet * 2) + balance

            print("")
            print("your balance", balance)

