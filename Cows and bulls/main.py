import random

digit_1 = str(random.randint(0, 9))
digit_2 = str(random.randint(0, 9))
digit_3 = str(random.randint(0, 9))
digit_4 = str(random.randint(0, 9))


count = 0
while True:
    while True:
        guess = input("guess a 4 digit number ")  # not an int input to pervent error

        if len(guess) == 4:
            break
        else:
            print("Thats not 4 digits")

    guess_1 = guess[0]
    guess_2 = guess[1]
    guess_3 = guess[2]
    guess_4 = guess[3]

    bull = 0
    cow = 0

    if guess_1 in [digit_1, digit_2, digit_3, digit_4]:
        cow = cow + 1
        if guess_1 == digit_1:
            bull = bull + 1

    if guess_2 in [digit_1, digit_2, digit_3, digit_4]:
        cow = cow + 1
        if guess_1 == digit_1:
            bull = bull + 1

    if guess_3 in [digit_1, digit_2, digit_3, digit_4]:
        cow = cow + 1
        if guess_1 == digit_1:
            bull = bull + 1

    if guess_4 in [digit_1, digit_2, digit_3, digit_4]:
        cow = cow + 1
        if guess_1 == digit_1:
            bull = bull + 1

    print(f"There are {cow} cow(s) meaning there {cow} digits that exist int the random number ")
    print(f"There are {bull} bull(s) meaning there {bull} digits that are in the right place ")

    count = count + 1

    if bull == 4:
        print("you finsihed in", count, "tries")
        break
    print("attempt number: " , count)
    print("")