import random

target = int(input("What number would you like to go to"))
player1_score = 0
player2_score = 0

while True:
    player1_roll = random.randint(1, 6)
    print("player 1 rolled", player1_roll)

    if player1_roll == 1:
        print("your turn ended with 0 ", )
        player1_score = 0
        break
    else:
        player1_score = player1_score + player1_roll
        print("")
        print(f"you now have {player1_score}")

        stop = input("Carry on y/n").lower()
        if player1_score == target:
            player1_score = 500
            break
        if player1_score > target:
            player1_score = 0

        if stop == "n":
            print("Now its player 2s turn")
            break

while True:
    input("press any key to roll")
    player2_roll = random.randint(1, 6)
    print("player 2 rolled", player1_roll)

    if player2_roll == 1:
        print("your turn ended with 0")
        player2_score = 0
        break
    else:
        player2_score = player2_score + player2_roll
        print("")
        print(f"you now have {player2_score}")
        stop = input("Carry on y/n").lower()

        if player1_score == target:
            player2_score = 500
            break
        if player2_score > target:
            player1_score = 0
            break

        if stop == "y":
            break

if player1_score > player2_score:
    print("player 1 , is the winner")

elif player1_score < player2_score:
    print("player 2 , is the winner")
else:
    print("its a draw")
